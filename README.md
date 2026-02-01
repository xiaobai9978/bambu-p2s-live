# Bambu-P2S-Live 🚀

[![Docker Pulls](https://img.shields.io/docker/pulls/xiaobai9978/bambu-p2s-live)](https://hub.docker.com/r/xiaobai9978/bambu-p2s-live)
[![Docker Image Version](https://img.shields.io/docker/v/xiaobai9978/bambu-p2s-live?label=version)](https://hub.docker.com/r/xiaobai9978/bambu-p2s-live)

**Bambu-P2S-Live** 是一个轻量级的 Docker 桥接工具，专为 **拓竹 (Bambu Lab) P1 / P2 / A1** 系列打印机开发。它能自动唤醒打印机隐藏的视频端口，并将其转换为标准 RTSP 协议，解决局域网模式下视频流难以获取的问题。

---

## ✨ 核心功能

- **自动化唤醒**：内置守护进程，自动定期发送 MQTT 指令激活打印机视频流，防止端口关闭。
- **协议转换**：将拓竹非标加密的 `RTSPS` 转换为通用标准 `RTSP`。
- **多端口适配**：自动探测 `322` 和 `8854` 端口，适配不同固件版本。
- **全平台支持**：支持 VLC、PotPlayer、Home Assistant 以及浏览器直接观看。

---

## 🛠️ 快速上手

### 1. 准备工作
请确保打印机已开启 **局域网模式 (LAN Mode)**，并准备好以下参数：
- `PRINTER_IP`: 打印机的局域网 IP
- `ACCESS_CODE`: 8 位访问码
- `SERIAL_NUMBER`: 打印机序列号 (SN)

### 2. 使用 Docker Compose (推荐)
```yaml
services:
  bambu-live:
    image: xiaobai9978/bambu-p2s-live:latest
    container_name: bambu-p2s-live
    restart: unless-stopped
    ports:
      - "8554:8554" # RTSP 播放端口
      - "1984:1984" # 网页预览/控制台
    environment:
      - PRINTER_IP=192.168.1.100     # 填入打印机IP
      - ACCESS_CODE=87654321         # 填入访问码
      - SERIAL_NUMBER=01P00XXXXXXXX  # 填入SN码



### 📺 观看方式

| 观看方式 | 播放地址 (URL) | 推荐工具 |
| :--- | :--- | :--- |
| **标准 RTSP** | `rtsp://宿主机IP:8554/live` | PotPlayer, VLC, OBS, HA |
| **网页直接看** | `http://宿主机IP:1984/stream.html?src=live` | Chrome, Firefox, 手机浏览器 |
| **控制台预览** | `http://宿主机IP:1984` | Go2RTC 后台管理 |
