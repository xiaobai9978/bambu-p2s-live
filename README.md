cat <<'EOF' > README.md
# Bambu-P2S-Live

Bambu-P2S-Live 是一个 Docker 工具，专门用于将拓竹 P1/P2/A1 系列打印机的视频流转换为标准 RTSP。

## 功能介绍
1. 自动发送 MQTT 指令唤醒打印机摄像头。
2. 将加密视频流转为标准 RTSP 地址。
3. 支持网页直接预览监控。

## 运行方式 (Docker Compose)

services:
  bambu-live:
    image: xiaobai9978/bambu-p2s-live:latest
    container_name: bambu-p2s-live
    restart: unless-stopped
    ports:
      - "8554:8554"
      - "1984:1984"
    environment:
      - PRINTER_IP=192.168.1.100
      - ACCESS_CODE=87654321
      - SERIAL_NUMBER=01P00XXXXXXXX

## 播放地址

RTSP 地址: rtsp://你的IP:8554/live
网页预览: http://你的IP:1984/stream.html?src=live
管理界面: http://你的IP:1984

## 注意事项
请确保打印机开启了局域网模式，且填写的访问码和 IP 正确。
EOF
