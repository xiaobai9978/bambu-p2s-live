#!/bin/bash
set -e
echo "[Bambu-Bridge] Starting Wake-up Service..."
python3 -u /app/wake_up.py &
echo "[Bambu-Bridge] Starting Go2RTC Server..."
exec /app/go2rtc -config /app/go2rtc.yaml
