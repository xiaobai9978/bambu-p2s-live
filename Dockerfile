FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y curl dos2unix && rm -rf /var/lib/apt/lists/*
RUN pip install paho-mqtt
RUN curl -L https://github.com/AlexxIT/go2rtc/releases/download/v1.9.4/go2rtc_linux_amd64 -o /app/go2rtc \
    && chmod +x /app/go2rtc
COPY wake_up.py .
COPY go2rtc.yaml .
COPY entrypoint.sh .
RUN dos2unix entrypoint.sh && chmod +x entrypoint.sh
ENV STREAM_NAME=live
EXPOSE 8554 1984
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
