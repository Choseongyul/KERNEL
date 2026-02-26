import time
import logging
import clickhouse_connect
from datetime import datetime, timedelta

# ================= Configuration =================
CHECK_INTERVAL = 60         # 1분마다 검사
LOOKBACK_MINUTES = 5        # 최근 5분 데이터 조회
CONTEXT_WINDOW_MINUTES = 5  # 탐지 시 전후 5분 저장

# DB 설정 (환경에 맞게 수정)
DB_HOST = 'localhost'
DB_PORT = 8123
DB_USER = 'default'
DB_PASSWORD = ''
# =================================================

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s [%(levelname)s] [BASELINE] %(message)s'
)

def get_client():
    return clickhouse_connect.get_client(host=DB_HOST, port=DB_PORT, username=DB_USER, password=DB_PASSWORD)

def preserve_context(client, trigger_ip, detection_time):
    """
    [Context Preservation]
    IP 기준으로 양방향 로그 수집 -> Flow UUID로 중복 제거
    """
    if isinstance(detection_time, str):
        detection_dt = datetime.strptime(detection_time, '%Y-%m-%d %H:%M:%S')
    else:
        detection_dt = detection_time

    start_dt = detection_dt - timedelta(minutes=CONTEXT_WINDOW_MINUTES)
    end_dt = detection_dt + timedelta(minutes=CONTEXT_WINDOW_MINUTES)

    query = f"""
    INSERT INTO network_incidents
    SELECT * FROM hubble
    WHERE 
      (src_ip = '{trigger_ip}' OR dest_ip = '{trigger_ip}')
      AND time BETWEEN '{start_dt}' AND '{end_dt}'
      AND flow_uuid NOT IN (
          SELECT flow_uuid FROM network_incidents 
          WHERE time BETWEEN '{start_dt}' AND '{end_dt}'
      )
    """
    client.command(query)
    logging.info(f" -> Evidence saved for {trigger_ip}")

def run():
    client = get_client()
    logging.info("Baseline Monitor Started...")
    
    while True:
        try:
            # Baseline 위반 탐지 쿼리
            query = f"""
            SELECT DISTINCT 
                log.src_ip, log.dest_ip, log.dest_port, log.src_pod, min(log.time) as first_seen
            FROM hubble AS log
            LEFT JOIN baseline_hubble AS base
            ON log.src_ip = base.src_ip 
               AND log.dest_ip = base.dest_ip 
               AND log.src_pod = base.src_pod
            WHERE log.time >= now() - INTERVAL {LOOKBACK_MINUTES} MINUTE
              AND base.src_ip = '' -- Whitelist에 없는 경우
              AND log.src_ip NOT IN (
                  SELECT src_ip FROM network_incidents
                  WHERE time >= now() - INTERVAL 10 MINUTE
              )
            GROUP BY log.src_ip, log.dest_ip, log.dest_port, log.src_pod
            """
            rows = client.query(query).result_rows

            for row in rows:
                src, dst, port, pod, first_seen = row
                logging.warning(f"VIOLATION: {src}({pod}) -> {dst}:{port}")
                preserve_context(client, src, first_seen)

        except Exception as e:
            logging.error(f"Error: {e}")
            # DB 연결 끊김 등 대비해 클라이언트 재연결 시도 로직이 필요할 수 있음
            try:
                client = get_client()
            except:
                pass

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run()