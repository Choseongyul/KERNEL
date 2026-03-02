import sys
import os
import re
import queue
import threading
import json
import io
import time
import uuid
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from contextlib import redirect_stdout

import uvicorn
import requests
import urllib3
import clickhouse_connect
from fastapi import FastAPI, Request

# ==============================================================================
# 설정 (Configuration)
# ==============================================================================
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# OpenSearch 설정
OS_HOST = ""
OS_USER = ""
OS_PASS = ""

# ClickHouse 설정
CH_HOST = ""
CH_PORT = 8123
CH_USER = ""
CH_PASS = ""

# 성능 설정
NUM_WORKERS = 4         
MAX_QUEUE_SIZE = 0      # 0 = 무제한 (메모리 30GB 환경 권장)
REPORT_DIR = os.path.expanduser("~/alerts")

ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

# UI Colors (Terminal Output용)
C_BLUE    = "\033[94m"
C_GREEN   = "\033[92m"
C_YELLOW  = "\033[93m"
C_CYAN    = "\033[96m"
C_MAGENTA = "\033[95m"
C_WHITE   = "\033[97m"
C_BOLD    = "\033[1m"
C_RED     = "\033[91m"
C_END     = "\033[0m"

app = FastAPI()
job_queue = queue.Queue(maxsize=MAX_QUEUE_SIZE)

# ==============================================================================
# [Core Logic 1] ClickHouse Analysis Class
# ==============================================================================
class SecurityAnalyzer:
    def __init__(self, host, port, user, password):
        try:
            self.client = clickhouse_connect.get_client(
                host=host, port=port, username=user, password=password, database="default"
            )
            print(f"[DB] Connected to ClickHouse ({threading.current_thread().name})")
        except Exception as e:
            print(f"[CRITICAL] ClickHouse Connection Failed: {e}")
            raise e

    def query_one(self, sql: str, params: Dict) -> Optional[Dict]:
        try:
            result = self.client.query(sql, parameters=params)
            if result.result_rows:
                return dict(zip(result.column_names, result.result_rows[0]))
            return None
        except Exception as e:
            print(f"[ERROR] Query Failed: {e}")
            return None

    def query_all(self, sql: str, params: Dict) -> List[Dict]:
        try:
            result = self.client.query(sql, parameters=params)
            return [dict(zip(result.column_names, r)) for r in result.result_rows]
        except Exception:
            return []

    def get_anchor_event(self, exec_id: str, event_type: str, target_time: str = None) -> Optional[Dict]:
        sql = """
        SELECT time, log_id, node_name, exec_id, parent_exec_id, binary, arguments, flags,
               uid, auid, pod_name, namespace, container_name, container_image, container_id,
               parent_binary, function_name, syscall_args, policy_name, action
        FROM default.tetragon
        WHERE exec_id = {exec_id:String}
        """
        params = {"exec_id": exec_id}

        if event_type and event_type != "other":
            sql += " AND event_type = {evt:String} "
            params["evt"] = event_type

        if target_time:
            sql += " ORDER BY abs(toFloat64(time) - toFloat64(parseDateTime64BestEffort({ts:String}))) ASC LIMIT 1"
            params["ts"] = target_time
        else:
            sql += " ORDER BY time DESC LIMIT 1 "
            
        return self.query_one(sql, params)

    def get_process_tree(self, exec_id: str) -> List[Dict]:
        # Recursive CTE를 사용하여 부모와 자식 프로세스 전체 추적
        sql = """
        WITH RECURSIVE
        ancestors AS (
            SELECT time, exec_id, parent_exec_id, binary, arguments, uid, 0 AS level
            FROM default.tetragon WHERE exec_id = {eid:String}
            UNION ALL
            SELECT t.time, t.exec_id, t.parent_exec_id, t.binary, t.arguments, t.uid, a.level - 1
            FROM default.tetragon t JOIN ancestors a ON t.exec_id = a.parent_exec_id
        ),
        family AS (
            SELECT time, exec_id, parent_exec_id, binary, arguments, uid, level FROM ancestors
            UNION ALL
            SELECT t.time, t.exec_id, t.parent_exec_id, t.binary, t.arguments, t.uid, f.level + 1
            FROM default.tetragon t JOIN family f ON t.parent_exec_id = f.exec_id
        )
        SELECT DISTINCT time, exec_id, parent_exec_id, binary, arguments, uid
        FROM family ORDER BY time LIMIT 1 BY exec_id
        """
        rows = self.query_all(sql, {"eid": exec_id})
        
        if not rows:
            fallback_sql = """
            SELECT time, exec_id, parent_exec_id, binary, arguments, uid
            FROM default.tetragon
            WHERE parent_exec_id = (
                SELECT parent_exec_id FROM default.tetragon WHERE exec_id = {eid:String} LIMIT 1
            )
            ORDER BY time LIMIT 1 BY exec_id
            """
            return self.query_all(fallback_sql, {"eid": exec_id})
        return rows

def generate_tree_output(procs: List[Dict], anchor_id: str, buffer):
    if not procs:
        print("[-] No process lineage found.", file=buffer)
        return

    by_parent = {}
    all_ids = set()
    for p in procs:
        by_parent.setdefault(p["parent_exec_id"], []).append(p)
        all_ids.add(p["exec_id"])

    roots = [p for p in procs if p["parent_exec_id"] not in all_ids]
    if not roots and procs:
        procs.sort(key=lambda x: x['time'])
        roots = [procs[0]]

    print(f"{C_BOLD}{'TIME':<10} {'UID':<5} {'CMD'}{C_END}", file=buffer)
    print("-" * 120, file=buffer)

    def walk(node, indent="", last=True):
        mark = "└─ " if last else "├─ "
        is_anchor = node["exec_id"] == anchor_id
        
        if is_anchor:
            color = C_GREEN + C_BOLD; id_color = C_GREEN
            suffix = f" {C_RED}[<-- TRIGGER EVENT]{C_END}"
        else:
            color = C_WHITE; id_color = C_CYAN
            suffix = ""
        
        uid_color = C_RED if node["uid"] == 0 else C_CYAN
        ts = node["time"].strftime("%H:%M:%S")
        cmd_str = f"{node['binary']} {node['arguments']}"
        exec_id_str = f"(ID: {node['exec_id']})"
        
        prefix = f"{C_BLUE}{ts:<10}{C_END} {uid_color}{str(node['uid']):<5}{C_END} "
        
        print(f"{prefix}{indent}{mark}{color}{cmd_str}{C_END} {id_color}{exec_id_str}{C_END}{suffix}", file=buffer)

        children = by_parent.get(node["exec_id"], [])
        children.sort(key=lambda x: x['time'])
        for i, c in enumerate(children):
            walk(c, indent + ("    " if last else "│  "), i == len(children) - 1)

    for root in roots:
        walk(root)

# ==============================================================================
# [Core Logic 2] Report Generator
# ==============================================================================
def perform_analysis(analyzer: SecurityAnalyzer, exec_id: str, event_type: str, start_time: str) -> str:
    output_buffer = io.StringIO()
    
    try:
        anchor = analyzer.get_anchor_event(exec_id, event_type, start_time)
        if not anchor:
            return f"[ERROR] Execution ID not found: {exec_id} (Type: {event_type})"

        print(f"\n{C_BOLD}[*] SECURITY INCIDENT DETAIL{C_END}", file=output_buffer)
        print(f"Time      : {anchor['time']}", file=output_buffer)
        print(f"Trigger   : {C_RED}{event_type.upper()}{C_END}", file=output_buffer)
        print(f"Pod       : {C_MAGENTA}{anchor['pod_name']}{C_END} (NS: {anchor['namespace']})", file=output_buffer)
        print(f"Node      : {anchor['node_name']}", file=output_buffer)
        print(f"User      : UID={anchor['uid']} / AUID={anchor['auid']}", file=output_buffer)
        
        print(f"\n{C_BOLD}[*] Event Details{C_END}", file=output_buffer)
        print(f"Binary    : {C_RED}{anchor['binary']}{C_END}", file=output_buffer)
        print(f"Args      : {anchor['arguments']}", file=output_buffer)
        print(f"Exec ID   : {exec_id}", file=output_buffer)
        
        if anchor['function_name']:
            print(f"Syscall   : {C_YELLOW}{anchor['function_name']}{C_END}", file=output_buffer)
        if anchor['policy_name']:
            print(f"Policy    : {C_RED}{anchor['policy_name']} ({anchor['action']}){C_END}", file=output_buffer)

        print(f"\n{C_BOLD}[*] Process Lineage (Ancestors){C_END}", file=output_buffer)
        
        lineage = analyzer.get_process_tree(exec_id)
        generate_tree_output(lineage, exec_id, output_buffer)
        
        return output_buffer.getvalue()
        
    except Exception as e:
        return f"[FATAL ERROR] Analysis Logic Failed: {str(e)}"
    finally:
        output_buffer.close()

def save_report_file(trigger: str, exec_id: str, event_type: str, content: str):
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    safe_trigger = re.sub(r'[^a-zA-Z0-9]', '_', trigger)
    safe_id = exec_id.replace("/", "_").replace("=", "")[-10:]
    safe_type = event_type.upper() if event_type else "UNKNOWN"
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    random_suffix = uuid.uuid4().hex[:6]
    
    filename = f"{REPORT_DIR}/alert_{timestamp}_{safe_trigger}_{safe_type}_{safe_id}_{random_suffix}.txt"
    clean_content = ANSI_ESCAPE.sub('', content)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"==========================================================\n")
        f.write(f"[*] ALERT TRIGGER : {trigger}\n")
        f.write(f"[*] EVENT TYPE    : {safe_type}\n")
        f.write(f"[*] DETECTED AT   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"==========================================================\n\n")
        f.write(clean_content)
    
    print(f"[FILE] Saved: {filename}")

# ==============================================================================
# [Core Logic 3] OpenSearch Context Fetcher
# ==============================================================================
def fetch_tetragon_context(doc_id: str, index_name: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    url = f"{OS_HOST}/{index_name}/_doc/{doc_id}"
    try:
        r = requests.get(url, auth=(OS_USER, OS_PASS), verify=False, timeout=5)
        if r.status_code != 200:
            print(f"[OS ERROR] Status: {r.status_code} | Doc: {doc_id}")
            return None, None, None

        src = r.json().get("_source", {})
        event_type, exec_id, start_time = "other", None, None

        if "process_exec" in src:
            event_type = "exec"
            proc = src["process_exec"].get("process", {})
            exec_id = proc.get("exec_id")
            start_time = proc.get("start_time")
        elif "process_exit" in src:
            event_type = "exit"
            proc = src["process_exit"].get("process", {})
            exec_id = proc.get("exec_id")
            start_time = proc.get("start_time")
        elif "process_kprobe" in src:
            event_type = "kprobe"
            proc = src["process_kprobe"].get("process", {})
            exec_id = proc.get("exec_id")
            start_time = proc.get("start_time")

        return exec_id, event_type, start_time
    except Exception as e:
        print(f"[OS EXCEPTION] {e}")
        return None, None, None

# ==============================================================================
# [Core Logic 4] Thread Worker
# ==============================================================================
def worker_main():
    thread_name = threading.current_thread().name
    print(f"[WORKER] Started {thread_name}")

    try:
        analyzer = SecurityAnalyzer(CH_HOST, CH_PORT, CH_USER, CH_PASS)
    except Exception:
        print(f"[FATAL] Worker {thread_name} died due to DB connection failure.")
        return

    while True:
        try:
            doc_id, index_name, trigger = job_queue.get()
            exec_id, event_type, start_time = fetch_tetragon_context(doc_id, index_name)

            if exec_id and start_time:
                print(f"[{thread_name}] Analyzing [{event_type.upper()}] {trigger} ({exec_id})")
                analysis_result = perform_analysis(analyzer, exec_id, event_type, start_time)
                save_report_file(trigger, exec_id, event_type, analysis_result)
            else:
                print(f"[{thread_name}] Context Not Found for Doc: {doc_id}")

        except Exception as e:
            print(f"[{thread_name}] Unexpected Error: {e}")
        finally:
            job_queue.task_done()

# ==============================================================================
# FastAPI App Startup & Endpoint
# ==============================================================================
@app.on_event("startup")
async def startup_event():
    print(f"[STARTUP] Initializing {NUM_WORKERS} workers with Persistent DB Connections...")
    for i in range(NUM_WORKERS):
        t = threading.Thread(target=worker_main, name=f"Worker-{i+1}", daemon=True)
        t.start()

@app.post("/webhook")
async def receive_webhook(request: Request):
    try:
        raw = (await request.body()).decode(errors="ignore").strip()
    except Exception as e:
        print(f"[Webhook ERROR] Body Read Failed: {e}")
        return {"status": "error", "reason": "body_read_failed"}

    docs_list, trigger = [], "Unknown"

    try:
        payload = json.loads(raw)
        trigger = payload.get("trigger", "Unknown")
        docs = payload.get("docs")
        
        if isinstance(docs, list): docs_list = docs
        elif isinstance(docs, str): docs_list = [docs]
        
    except json.JSONDecodeError as je:
        print(f"[Webhook WARN] JSON Decode Failed: {je} | Trying Regex fallback")
        t_m = re.search(r'"trigger"\s*:\s*"([^"]+)"', raw)
        d_m = re.findall(r'"docs"\s*:\s*(?:\[)?([^\s}\]]+)', raw)
        if t_m: trigger = t_m.group(1)
        if d_m: docs_list = [d.replace('"', '').replace('[', '').replace(']', '').strip() for d in d_m]
    except Exception as e:
        print(f"[Webhook ERROR] Parsing Logic Failed: {e}")
        return {"status": "error", "reason": "parsing_failed"}

    if not docs_list:
        print("[Webhook INFO] No docs found in payload")
        return {"status": "ignored", "reason": "no_docs"}

    count = 0
    for doc_pair in docs_list:
        if "|" in doc_pair:
            doc_id, index_name = map(str.strip, doc_pair.split("|", 1))
            try:
                job_queue.put((doc_id, index_name, trigger), block=False)
                count += 1
            except queue.Full:
                print(f"[WARN] Queue Full! Dropping alert: {doc_id}")
                return {"status": "error", "reason": "queue_full"}

    current_q_size = job_queue.qsize()
    if count > 0:
        print(f"[Webhook] +{count} Jobs Added (Trigger: {trigger}) | Current Queue: {current_q_size}")
        return {"status": "queued", "count": count, "queue_size": current_q_size}
    
    return {"status": "ignored"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)