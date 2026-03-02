import os
import re
import sys
import glob
import clickhouse_connect
from datetime import datetime, timedelta
from collections import defaultdict

# ==============================================================================
# [CONFIG]
# ==============================================================================
ALERTS_DIR = os.path.expanduser("~/alerts/")
REPORT_SAVE_DIR = os.path.expanduser("~/summary")

# 사용자 관찰 기반 시간 윈도우 (-10초 ~ +120초)
TIME_WINDOW_PRE = 10
TIME_WINDOW_POST = 120
MAX_VISIBLE_NET_LOGS = 10

# ClickHouse Config
DB_HOST = ""
DB_PORT = 8123
DB_USER = ""
DB_PASSWORD = ""

class IncidentAnalyzer:
    def __init__(self):
        # 1. Process Alert Parsing
        self.re_proc_time = re.compile(r'Time\s*:\s*(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}(?:\.\d+)?)')
        self.re_proc_trigger = re.compile(r'\[\*\] ALERT TRIGGER\s*:\s*(.+)')
        self.re_proc_pod = re.compile(r'Pod\s*:\s*([^\s]+)')
        self.re_proc_binary = re.compile(r'Binary\s*:\s*([^\s]+)')
        # Args: 줄바꿈 전까지만 파싱 (Exec ID 혼입 방지)
        self.re_proc_args = re.compile(r'Args\s*:\s*([^\r\n]+)') 
        self.re_proc_execid = re.compile(r'Exec ID\s*:\s*([^\s]+)')
        
        # 2. Artifact Mining
        self.re_dev_tcp = re.compile(r'/dev/(?:tcp|udp)/([\d\.]+)/(\d+)')
        self.re_ipv4 = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
        self.re_domain = re.compile(r'(?:http[s]?://)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

        os.makedirs(REPORT_SAVE_DIR, exist_ok=True)
        self.md_lines = []
        self.client = self.get_db_client()

    def get_db_client(self):
        try:
            return clickhouse_connect.get_client(host=DB_HOST, port=DB_PORT, username=DB_USER, password=DB_PASSWORD)
        except Exception as e:
            print(f"[ERROR] DB Connection Failed: {e}")
            sys.exit(1)

    def add(self, line=""):
        self.md_lines.append(line)

    def save_report(self):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"summary_report_{timestamp}.md"
        filepath = os.path.join(REPORT_SAVE_DIR, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("\n".join(self.md_lines))
            print(f"[SUCCESS] Report generated: {filepath}")
        except Exception as e:
            print(f"[ERROR] Failed to save report: {e}")

    # --------------------------------------------------------------------------
    # Utils
    # --------------------------------------------------------------------------
    def parse_time(self, time_str):
        try:
            time_str = time_str.strip()
            if '.' in time_str:
                return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
            return datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None

    # --------------------------------------------------------------------------
    # Loaders & Miners
    # --------------------------------------------------------------------------
    def fetch_network_logs(self, start_dt, end_dt):
        s_time = start_dt - timedelta(seconds=TIME_WINDOW_PRE)
        e_time = end_dt + timedelta(seconds=TIME_WINDOW_POST)
        
        query = f"""
        SELECT 
            time, 
            src_ip, src_pod, 
            dest_ip, dest_pod, dest_port
        FROM network_incidents
        WHERE time BETWEEN '{s_time}' AND '{e_time}'
        """
        
        try:
            result = self.client.query(query)
            logs = []
            for row in result.result_rows:
                # 데이터 정규화 및 포맷팅
                src = row[2] if row[2] else f"EXTERNAL:{row[1]}"
                dst = row[4] if row[4] else f"EXTERNAL:{row[3]}"
                
                # Pod 이름 prefix 추출 (매칭용)
                def get_prefix(s):
                    s = s.replace("EXTERNAL:", "")
                    parts = s.split("-")
                    if len(parts) > 2: return "-".join(parts[:-2])
                    return s

                logs.append({
                    "timestamp": row[0],
                    "src_raw": src,
                    "src_norm": get_prefix(src),
                    "src_ip": row[1],
                    "dst_raw": f"{dst}:{row[5]}",
                    "dest_ip": row[3],
                    "dest_norm": get_prefix(dst),
                    "dest_port": row[5]
                })
            return logs
        except Exception as e:
            print(f"[ERROR] DB Query Error: {e}")
            return []

    def mine_artifacts(self, args_str):
        artifacts = {'ips': set(), 'domains': set(), 'ports': set()}
        if not args_str or args_str == "None": return artifacts
        
        for ip, port in self.re_dev_tcp.findall(args_str):
            artifacts['ips'].add(ip); artifacts['ports'].add(int(port))
        
        for ip in self.re_ipv4.findall(args_str):
            try: artifacts['ips'].add(ip)
            except ValueError: pass
            
        # Loose port parsing
        tokens = re.split(r'[\s:="\']', args_str)
        for token in tokens:
            if token.isdigit():
                val = int(token)
                if 1 <= val <= 65535: artifacts['ports'].add(val)

        return artifacts

    def parse_alert_file(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
            trigger_m = self.re_proc_trigger.search(content)
            time_m = self.re_proc_time.search(content)
            pod_m = self.re_proc_pod.search(content)
            binary_m = self.re_proc_binary.search(content)
            args_m = self.re_proc_args.search(content)
            exec_id_m = self.re_proc_execid.search(content)

            if not (trigger_m and time_m and pod_m): return None

            args_str = args_m.group(1).strip() if args_m else ""
            dt = self.parse_time(time_m.group(1).strip())
            if not dt: return None

            return {
                "timestamp": dt,
                "pod": pod_m.group(1).strip(),
                "exec_id": exec_id_m.group(1).strip() if exec_id_m else "Unknown",
                "binary": binary_m.group(1).strip(),
                "args": args_str,
                "artifacts": self.mine_artifacts(args_str)
            }
        except Exception: return None

    # --------------------------------------------------------------------------
    # Aggregation (Deduplication Logic added)
    # --------------------------------------------------------------------------
    def aggregate_sequential_events(self, raw_logs):
        # 1. Deduplicate by Exec ID
        # 여러 파일(KPROBE, EXIT 등)이 같은 exec_id를 공유할 경우 하나로 합침
        unique_executions = {}
        for log in raw_logs:
            eid = log['exec_id']
            if eid not in unique_executions:
                unique_executions[eid] = log
            else:
                # 이미 존재하는 exec_id라면 Artifacts만 병합 (더 많은 정보 수집)
                unique_executions[eid]['artifacts']['ips'].update(log['artifacts']['ips'])
                unique_executions[eid]['artifacts']['ports'].update(log['artifacts']['ports'])
                # 시간은 가장 빠른 시간 유지
                if log['timestamp'] < unique_executions[eid]['timestamp']:
                    unique_executions[eid]['timestamp'] = log['timestamp']

        # 딕셔너리를 다시 리스트로 변환 및 시간 정렬
        sorted_unique_logs = sorted(unique_executions.values(), key=lambda x: x['timestamp'])

        # 2. Group similar sequential commands (e.g., repeated curls)
        events = []
        if not sorted_unique_logs: return events
        
        current_event = None
        for log in sorted_unique_logs:
            if current_event is None:
                current_event = self._create_event(log)
                continue
            
            time_diff = (log['timestamp'] - current_event['last_seen']).total_seconds()
            is_same_context = (log['pod'] == current_event['pod'] and log['binary'] == current_event['binary'] and log['args'] == current_event['args'])

            if is_same_context and time_diff < 120:
                current_event['count'] += 1
                current_event['last_seen'] = log['timestamp']
                current_event['exec_ids'].append(log['exec_id'])
                current_event['artifacts']['ips'].update(log['artifacts']['ips'])
                current_event['artifacts']['ports'].update(log['artifacts']['ports'])
            else:
                events.append(current_event)
                current_event = self._create_event(log)
        if current_event: events.append(current_event)
        return events

    def _create_event(self, log):
        return {
            "pod": log['pod'], "binary": log['binary'], "args": log['args'],
            "count": 1, "first_seen": log['timestamp'], "last_seen": log['timestamp'],
            "exec_ids": [log['exec_id']], "artifacts": log['artifacts']
        }

    def correlate_network(self, event):
        # [DB Query]
        net_logs = self.fetch_network_logs(event['first_seen'], event['last_seen'])
        
        known_ips = event['artifacts']['ips']
        known_ports = event['artifacts']['ports']
        pod_prefix = "-".join(event['pod'].split("-")[:-2]) if len(event['pod'].split("-")) > 2 else event['pod']

        evidence_map = defaultdict(list)
        has_confirmed = False
        has_related = False

        for log in net_logs:
            match_type = None
            
            # 1. IP Match (Confirmed)
            if log['dest_ip'] in known_ips or log['src_ip'] in known_ips:
                match_type = "CONFIRMED"
            # 2. Port Match (Confirmed)
            elif log['dest_port'] in known_ports and log['dest_port'] > 1024:
                match_type = "CONFIRMED"
            # 3. Pod Context Match (Related)
            elif (pod_prefix in log['src_norm']) or (pod_prefix in log['dest_norm']):
                match_type = "RELATED"

            if match_type:
                flow_fmt = f"{log['src_raw']} -> {log['dst_raw']}"
                
                # [수정] CONFIRMED인 경우 전체 라인 Bold 처리
                if match_type == "CONFIRMED":
                    flow_fmt = f"**{flow_fmt}**"
                
                key = (match_type, flow_fmt)
                evidence_map[key].append(log)
                
                if match_type == "CONFIRMED": has_confirmed = True
                elif match_type == "RELATED": has_related = True

        final_evidence = {}
        if has_confirmed:
            state_txt = "CONFIRMED"
            for k, v in evidence_map.items():
                if k[0] == "CONFIRMED": final_evidence[k] = v
        elif has_related:
            state_txt = "CORRELATED"
            final_evidence = evidence_map
        else:
            state_txt = "INFO"

        return final_evidence, state_txt

    # --------------------------------------------------------------------------
    # Output & Sorting
    # --------------------------------------------------------------------------
    def sort_network_flows(self, items):
        def sort_key(item):
            (m_type, flow_fmt), logs = item
            
            # 포트 파싱
            port = 0
            clean_fmt = flow_fmt.replace('*', '') # 볼드 제거하고 파싱
            match = re.search(r':(\d+)$', clean_fmt)
            if match:
                port = int(match.group(1))
            
            score = 0
            if m_type == "CONFIRMED": score += 1000
            if port > 0: score += 500  # 0번 포트 밀어내기
            
            return (score, len(logs))

        return sorted(items, key=sort_key, reverse=True)

    def render_network_table(self, sorted_flows):
        for (m_type, flow_fmt), logs in sorted_flows:
            timestamps = [l['timestamp'] for l in logs]
            total_count = len(logs)
            
            timestamps.sort()
            start_t = timestamps[0].strftime('%H:%M:%S.%f')
            end_t = timestamps[-1].strftime('%H:%M:%S.%f')
            
            t_range = f"{start_t} - {end_t}" if start_t != end_t else f"{start_t}"
            
            # flow_fmt는 이미 correlate_network에서 볼드 처리됨
            self.add(f"| {t_range} | {flow_fmt} | {total_count} | {m_type} |")

    def run(self):
        print("Analyzing alerts & querying ClickHouse...")
        files = glob.glob(os.path.join(ALERTS_DIR, "alert_*.txt"))
        if not files: 
            print("No alert files found.")
            return
        
        parsed_logs = []
        for f in files:
            res = self.parse_alert_file(f)
            if res: parsed_logs.append(res)
        
        # [중요] exec_id 중복 제거 로직 포함된 aggregation 호출
        events = self.aggregate_sequential_events(parsed_logs)

        self.add("# Automated Incident Timeline Report")
        self.add(f"> **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.add(f"> **Total Events:** {len(events)}")
        self.add("")

        for i, ev in enumerate(events, 1):
            evidence_map, state_txt = self.correlate_network(ev)
            
            start_s = ev['first_seen'].strftime('%H:%M:%S.%f')
            end_s = ev['last_seen'].strftime('%H:%M:%S.%f')
            time_display = f"{start_s} - {end_s}" if start_s != end_s else f"{start_s}"
            
            exec_id = ev['exec_ids'][0]

            self.add(f"## {i}. [{state_txt}] {time_display}")
            self.add(f"**Pod:** `{ev['pod']}`  |  **Exec ID:** `{exec_id}`")
            
            cmd = f"{ev['binary']} {ev['args']}"
            self.add(f"\n**Command (x{ev['count']}):**")
            self.add("```bash")
            self.add(cmd)
            self.add("```")

            if ev['artifacts']['ips']:
                self.add(f"\n**Artifacts:** `{', '.join(ev['artifacts']['ips'])}`")

            if evidence_map:
                self.add("\n**Network Activity:**")
                table_head = "| Time | Flow | Count | Type |\n| :--- | :--- | :--- | :--- |"
                
                sorted_flows = self.sort_network_flows(evidence_map.items())
                
                visible_flows = sorted_flows[:MAX_VISIBLE_NET_LOGS]
                hidden_flows = sorted_flows[MAX_VISIBLE_NET_LOGS:]

                self.add(table_head)
                self.render_network_table(visible_flows)

                if hidden_flows:
                    self.add(f"\n<details><summary>View {len(hidden_flows)} more flows...</summary>\n")
                    self.add(table_head)
                    self.render_network_table(hidden_flows)
                    self.add("\n</details>")
            else:
                if state_txt != "INFO":
                    self.add("\n> **No correlated network traffic found.**")

            # SQL Query
            sql_start = ev['first_seen'] - timedelta(minutes=2)
            sql_end = ev['last_seen'] + timedelta(minutes=2)
            
            self.add("\n**Investigation Query:**")
            self.add("```sql")
            self.add(f"-- Process Detail\nSELECT * FROM tetragon WHERE exec_id='{exec_id}';")
            
            if state_txt == "CONFIRMED":
                ips = list(ev['artifacts']['ips'])
                if ips:
                    ip_cond = ", ".join([f"'{ip}'" for ip in ips])
                    self.add(f"-- Network Check (Confirmed)\nSELECT * FROM network_incidents WHERE time BETWEEN '{sql_start}' AND '{sql_end}' AND (dest_ip IN ({ip_cond}) OR src_ip IN ({ip_cond}));")
            elif state_txt == "CORRELATED":
                pod_name = ev['pod'].split('-')[0]
                self.add(f"-- Network Check (Pod Context)\nSELECT * FROM network_incidents WHERE time BETWEEN '{sql_start}' AND '{sql_end}' AND (src_pod LIKE '%{pod_name}%' OR dest_pod LIKE '%{pod_name}%');")
            self.add("```")
            self.add("\n---")

        self.save_report()

if __name__ == "__main__":
    IncidentAnalyzer().run()