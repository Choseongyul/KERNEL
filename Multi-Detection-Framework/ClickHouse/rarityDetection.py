import time
import json
from datetime import datetime, timezone
from collections import defaultdict
import clickhouse_connect

# ==========================================
# [Configuration] Settings
# ==========================================
INTERVAL = 60
STATE_FILE = "alert_state_rare.json"     # 프로그램용 (중복 방지 State)
LOG_FILE   = "security_log_rare.txt"     # 분석가용 (상세 이력 Log)

# Thresholds
RARE_THRESHOLD = 0.002       # 0.2% 미만
LOW_VOLUME_THRESHOLD = 2000  # 2000회 미만 (사각지대 보정)
DETAIL_LOOKBACK_HOURS = 24   # 상세 역추적 범위

# UI Colors
C_YELLOW  = "\033[93m"
C_BOLD    = "\033[1m"
C_RESET   = "\033[0m"

# ==========================================
# [Database] Connection
# ==========================================
client = clickhouse_connect.get_client(
    host="localhost",
    port=8123,
    user="admin",
    password="password",
    database="default"
)

# ==========================================
# [Functions] State & Logging
# ==========================================
def load_state():
    """로드: 이전에 탐지된 Exec ID 목록을 불러옵니다."""
    try:
        with open(STATE_FILE, "r") as f:
            return set(json.load(f))
    except:
        return set()

def save_state(state):
    """저장: 현재 탐지된 Exec ID 목록을 파일에 저장합니다."""
    with open(STATE_FILE, "w") as f:
        json.dump(list(state), f)

def append_log(data):
    """기록: 분석가를 위해 상세 내용을 텍스트 파일에 누적합니다."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"[{timestamp}] [WARNING] SUSPICIOUS PROCESS BEHAVIOR\n"
        f"  - Alert Type  : {data['tag']} {data['reason']}\n"
        f"  - Pod Name    : {data['pod']}\n"
        f"  - Binary      : {data['binary']}\n"
        f"  - Arguments   : {data['args']}\n"
        f"  - Count Ratio : {data['cnt']}/{data['total']}\n"
        f"  - Exec ID     : {data['id']}\n"
        f"{'-'*60}\n"
    )
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

# ==========================================
# [Main] Monitoring Loop
# ==========================================
seen = load_state()
print(f"[*] Hybrid Anomaly Monitor Started")
print(f"    - State File : {STATE_FILE}")
print(f"    - Log File   : {LOG_FILE}")

while True:
    try:
        # ---------------------------------------------------------
        # [Step 1] Statistical Analysis (Summary Table)
        # 통계적으로 의심스러운 (Pod, Binary) 그룹 식별
        # ---------------------------------------------------------
        summary_rows = client.query(f"""
            SELECT
                s.pod_name,
                s.binary,
                s.real_count,
                t.total_count,
                1.0 * s.real_count / t.total_count AS ratio
            FROM (
                SELECT pod_name, binary, SUM(exec_count) AS real_count
                FROM default.tetragon_summary
                WHERE pod_name != ''
                GROUP BY pod_name, binary
            ) AS s
            JOIN (
                SELECT pod_name, SUM(exec_count) AS total_count
                FROM default.tetragon_summary
                WHERE pod_name != ''
                GROUP BY pod_name
            ) AS t
            ON s.pod_name = t.pod_name
            WHERE 
                (t.total_count >= {LOW_VOLUME_THRESHOLD} AND ratio <= {RARE_THRESHOLD})
                OR 
                (t.total_count < {LOW_VOLUME_THRESHOLD})
        """).result_rows

        if not summary_rows:
            time.sleep(INTERVAL)
            continue

        # ---------------------------------------------------------
        # [Step 2] Context Enrichment (Raw Table)
        # 식별된 그룹에 대해 가장 최신 Exec ID와 인자값 역추적
        # ---------------------------------------------------------
        targets = []
        target_keys = set()
        details_map = defaultdict(lambda: {'id': None, 'args': '-'})

        for r in summary_rows:
            pod, binary = r[0], r[1]
            if (pod, binary) not in target_keys:
                targets.append(f"(pod_name = '{pod}' AND binary = '{binary}')")
                target_keys.add((pod, binary))
        
        if targets:
            where_condition = " OR ".join(targets)
            raw_rows = client.query(f"""
                SELECT 
                    pod_name,
                    binary,
                    argMax(exec_id, time) as latest_id,
                    argMax(arguments, time) as latest_args
                FROM default.tetragon
                WHERE ({where_condition})
                  AND event_type = 'exec'
                  AND time >= now() - toIntervalHour({DETAIL_LOOKBACK_HOURS})
                GROUP BY pod_name, binary
            """).result_rows

            for raw in raw_rows:
                details_map[(raw[0], raw[1])] = {'id': raw[2], 'args': raw[3]}

        # ---------------------------------------------------------
        # [Output] Alert Formatting & Deduplication
        # ---------------------------------------------------------
        new_alerts = False
        
        for r in summary_rows:
            pod, binary, cnt, total, ratio = r[0], r[1], r[2], r[3], r[4]
            
            detail = details_map[(pod, binary)]
            exec_id = detail['id']
            args = detail['args']

            # ID가 없거나(로그 만료) 이미 본 ID면 건너뜀
            if exec_id is None: 
                continue 
            
            key = f"rare:{exec_id}"
            if key in seen:
                continue
            
            seen.add(key)
            save_state(seen)
            new_alerts = True

            # 태그 및 원인 결정
            if total < LOW_VOLUME_THRESHOLD:
                tag = "[SILENT]"
                reason = f"Low Volume (<{LOW_VOLUME_THRESHOLD})"
            else:
                tag = "[RARE]  "
                reason = f"Rare Ratio ({ratio*100:.4f}%)"

            display_args = (args[:60] + '..') if args and len(args) > 60 else args

            # 화면 출력
            print(f"\n{'-'*65}")
            print(f"{C_YELLOW}{C_BOLD}[WARNING] SUSPICIOUS PROCESS BEHAVIOR{C_RESET}")
            print(f"{'-'*65}")
            print(f"  TYPE         : {tag} {reason}")
            print(f"  POD NAME     : {pod}")
            print(f"{'-'*65}")
            print(f"  BINARY       : {binary}")
            print(f"  ARGUMENTS    : {display_args}")
            print(f"  COUNT        : {cnt}/{total} (Run Count / Total Pod Activity)")
            print(f"{'-'*65}")
            print(f"  EXEC ID      : {exec_id}")
            print(f"{'='*65}")

            # 파일 기록 (분석가용)
            append_log({
                "tag": tag,
                "reason": reason,
                "pod": pod,
                "binary": binary,
                "args": args, # 파일에는 전체 인자 저장
                "cnt": cnt,
                "total": total,
                "id": exec_id
            })

        if new_alerts:
            current_time = datetime.now(timezone.utc).strftime("%H:%M:%S")
            print(f"[*] New anomaly logged to {LOG_FILE} at {current_time}")

        time.sleep(INTERVAL)

    except Exception as e:
        print(f"[ERROR] System Fault: {e}")
        time.sleep(5)