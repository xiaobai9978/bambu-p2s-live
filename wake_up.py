import paho.mqtt.client as mqtt
import json
import ssl
import os
import time
import sys

# 从环境变量获取配置
PRINTER_IP = os.getenv("PRINTER_IP")
ACCESS_CODE = os.getenv("ACCESS_CODE")
SERIAL_NUMBER = os.getenv("SERIAL_NUMBER")

if not all([PRINTER_IP, ACCESS_CODE, SERIAL_NUMBER]):
    print("错误: 缺少环境变量 PRINTER_IP, ACCESS_CODE 或 SERIAL_NUMBER")
    sys.exit(1)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"[MQTT] 已连接到打印机 {PRINTER_IP}，准备唤醒摄像头...")
        payload = {
            "camera": {"command": "setup", "resolution": "720p", "rtsp": "on"},
            "user_id": "0"
        }
        topic = f"device/{SERIAL_NUMBER}/report"
        client.publish(topic, json.dumps(payload))
        print(f"[MQTT] 唤醒指令已发送至 {topic}")
    else:
        print(f"[MQTT] 连接失败，错误码: {rc}")

def on_disconnect(client, userdata, rc):
    print("[MQTT] 连接断开，尝试重连...")

client = mqtt.Client()
client.username_pw_set("bblp", ACCESS_CODE)
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.tls_insecure_set(True)
client.on_connect = on_connect
client.on_disconnect = on_disconnect

print(f"[System] 启动 MQTT 守护进程，目标: {PRINTER_IP}")

while True:
    try:
        client.connect(PRINTER_IP, 8883, 60)
        client.loop_forever()
    except Exception as e:
        print(f"[Error] 连接异常: {e}，5秒后重试...")
        time.sleep(5)
