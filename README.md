Bambu-P2S-Live 🚀

Bambu-P2S-Live 是一个轻量级的 Docker 桥接工具，专门为 拓竹 (Bambu Lab) P1P / P1S / P2S / A1 系列打印机开发。它能自动唤醒打印机隐藏的局域网视频流，并将其转换为标准 RTSP 协议，让你可以在任何播放器或智能家居系统中轻松监控打印状态。
✨ 核心功能

    自动化唤醒：内置 MQTT 守护进程，自动发送握手指令激活打印机视频端口。

    协议转换：将非标加密的 RTSPS 转换为通用标准 RTSP。

    多端口兼容：自动扫描 322 和 8854 端口，适配不同版本的拓竹固件。

    低延迟转发：基于 Go2RTC 技术栈，提供几乎无感的实时监控体验。

    网页预览：无需安装播放器，直接通过浏览器即可查看监控画面。

🛠️ 快速上手
1. 环境准备

确保你的打印机已开启 局域网模式 (LAN Mode)，并记录以下信息：

    IP 地址: 打印机的局域网 IP。

    访问码 (Access Code): 8 位局域网验证码。

    序列号 (Serial Number): 15 位打印机 SN 码。

2. 使用 Docker Compose (推荐)

创建一个 docker-compose.yml 文件：
YAML

services:
  bambu-live:
    image: xiaobai9978/bambu-p2s-live:latest
    container_name: bambu-p2s-live
    restart: unless-stopped
    ports:
      - "8554:8554" # RTSP 播放端口
      - "1984:1984" # Web 管理界面
    environment:
      - PRINTER_IP=192.168.1.100     # 替换为你的打印机 IP
      - ACCESS_CODE=87654321          # 替换为你的访问码
      - SERIAL_NUMBER=01Pxxxxxxxxxxxx # 替换为你的 SN 码

执行命令启动：
Bash

docker-compose up -d

3. 使用 Docker Run
Bash

docker run -d \
  --name bambu-live \
  -p 8554:8554 \
  -p 1984:1984 \
  -e PRINTER_IP=你的IP \
  -e ACCESS_CODE=你的访问码 \
  -e SERIAL_NUMBER=你的SN \
  xiaobai9978/bambu-p2s-live:latest

📺 观看视频流
观看方式	地址格式	适用工具
标准 RTSP	rtsp://宿主机IP:8554/live	PotPlayer, VLC, OBS, IINA
网页预览	http://宿主机IP:1984/stream.html?src=live	Chrome, Firefox, Safari
管理后台	http://宿主机IP:1984	查看运行状态和链路信息
❓ 常见问题 (FAQ)

Q: 为什么 8554 端口在浏览器里打不开？ A: 8554 是 RTSP 专有端口，浏览器不支持该协议。网页观看请务必使用 1984 端口。

Q: 画面加载很慢或黑屏？ A: 请确保打印机和 Docker 宿主机在同一个网段。如果正在使用 Bambu Handy App 观看，可能会因为打印机带宽限制导致 Docker 端断开。

Q: 支持 Home Assistant 吗？ A: 完美支持！在 HA 中添加 Generic Camera 集成，填入 rtsp://宿主机IP:8554/live 即可。
🤝 贡献与反馈

如果你在测试中发现了 BUG，或者希望支持更多型号，欢迎提交 Issue。 如果这个项目帮到了你，请给一个 Star 🌟，这是对我最大的鼓励！
