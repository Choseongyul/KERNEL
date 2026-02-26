import json
import subprocess
import uvicorn
import requests
import urllib3
import re
from fastapi import FastAPI, Request
from typing import Optional, Tuple

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = FastAPI()

# 저장된 파일명과 일치해야 합니다 (예: clickhouse.py)
ANALYZER_SCRIPT = "clickhouse.py"

# [수정] OpenSearch IP 변경
OS_HOST = "https://10.0.1.141:9200"
OS_USER = "admin"
OS_PASS = "Aadmin123!"

# ==============================================================================
# OpenSearch → exec_id 추출 (Tetragon 전용)
# ==============================================================================
def fetch_tetragon_context(doc_id: str, index_name: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    url = f"{OS_HOST}/{index_name}/_doc/{doc_id}"

    try:
        r = requests.get(url, auth=(OS_USER, OS_PASS), verify=False, timeout=5)
        if r.status_code != 200:
            print(f"[ERROR] OpenSearch fetch failed: {r.status_code}")
            return None, None, None

        src = r.json().get("_source", {})
        
        timestamp = src.get("@timestamp")

        event_type = "other"
        exec_id = None

        if "process_exec" in src:
            event_type = "exec"
            exec_id = src["process_exec"]["process"].get("exec_id")
        elif "process_exit" in src:
            event_type = "exit"
            exec_id = src["process_exit"]["process"].get("exec_id")
        elif "process_kprobe" in src:
            event_type = "kprobe"
            exec_id = src["process_kprobe"]["process"].get("exec_id")

        return exec_id, event_type, timestamp

    except Exception as e:
        print(f"[ERROR] OpenSearch exception: {e}")
        return None, None, None


# ==============================================================================
# Webhook Receiver
# ==============================================================================
@app.post("/webhook")
async def receive_webhook(request: Request):
    raw = (await request.body()).decode(errors="ignore").strip()

    trigger = None
    doc_pair = None

    try:
        payload = json.loads(raw)
        trigger = payload.get("trigger")
        docs = payload.get("docs")

        if isinstance(docs, list) and docs:
            doc_pair = docs[0]
        elif isinstance(docs, str):
            doc_pair = docs

    except json.JSONDecodeError:
        trigger_match = re.search(r'"trigger"\s*:\s*"([^"]+)"', raw)
        docs_match = re.search(r'"docs"\s*:\s*([^\s}]+)', raw)

        if trigger_match:
            trigger = trigger_match.group(1)
        if docs_match:
            doc_pair = docs_match.group(1)

    if not trigger or not doc_pair or "|" not in doc_pair:
        print("[WARN] Invalid webhook payload")
        return {"status": "ignored"}

    doc_id, index_name = map(str.strip, doc_pair.split("|", 1))

    print("=" * 60)
    print(f"Trigger     : {trigger}")
    print(f"_id         : {doc_id}")
    print(f"Index       : {index_name}")

    # ==========================================================================
    # 인덱스 이름으로 분기 처리 (Early Return 적용)
    # ==========================================================================
    
    # 1. Hubble 로그일 경우
    if "hubble" in index_name:
        print(f"[INFO] Hubble Log detected via index name.")
        print(">> Skipping execution analysis for Hubble.")
        print("=" * 60)
        return {"status": "hubble_skipped"}

    # 2. Tetragon 로그일 경우
    elif "tetragon" in index_name:
        print(f"[INFO] Tetragon Log detected via index name.")
        
        # Tetragon 로직 수행
        exec_id, event_type, timestamp = fetch_tetragon_context(doc_id, index_name)

        if not exec_id or not timestamp:
            print("[ERROR] Context missing (exec_id or timestamp)")
            print("=" * 60)
            return {"status": "failed"}

        print(f"Exec ID     : {exec_id}")
        print(f"Event Type  : {event_type}")
        print(f"Timestamp   : {timestamp}")
        print("=" * 60)

        subprocess.run(
            ["python3", ANALYZER_SCRIPT, exec_id, event_type, str(timestamp)],
            capture_output=False
        )
        print("=" * 60)
        return {"status": "success"}

    # 3. 그 외 알 수 없는 인덱스
    else:
        print(f"[WARN] Unknown index pattern: {index_name}")
        print("=" * 60)
        return {"status": "unknown_ignored"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
