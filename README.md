# Bambu-P2S-Live 🚀

[![Docker Pulls](https://img.shields.io/docker/pulls/xiaobai9978/bambu-p2s-live)](https://hub.docker.com/r/xiaobai9978/bambu-p2s-live)
[![Docker Image Version](https://img.shields.io/docker/v/xiaobai9978/bambu-p2s-live?label=version)](https://hub.docker.com/r/xiaobai9978/bambu-p2s-live)

**Bambu-P2S-Live** 是一个轻量级的 Docker 桥接工具，专为 **拓竹 (Bambu Lab) P1 / P2 / A1** 系列打印机开发。它能自动唤醒打印机隐藏的视频端口，并将其转换为标准 RTSP 协议。

---

## ✨ 核心功能

- **自动化唤醒**：内置守护进程，自动发送 MQTT 指令激活打印机视频流。
- **协议转换**：将加密的 `RTSPS` 转换为标准 `RTSP`。
- **多端口兼容**：自动适配 322 和 8854 端口。
- **网页预览**：支持通过浏览器直接查看监控画面。

---

## 🛠️ 快速上手

### 1. 环境变量配置
请确保打印机已开启 **局域网模式**，并准备好以下参数：
- `PRINTER_IP`: 打印机 IP 地址
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
      - "8554:8554" # RTSP 播放
      - "1984:1984" # 网页预览
    environment:
      - PRINTER_IP=192.168.x.x
      - ACCESS_CODE=xxxxxxxx
      - SERIAL_NUMBER=01Pxxxxxxxxxxxx
