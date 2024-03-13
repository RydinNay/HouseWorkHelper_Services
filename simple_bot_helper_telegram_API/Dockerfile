FROM python:3.10
WORKDIR /app

ENV bot_token = ""
ENV WEB_SERVER_HOST = ""
ENV WEB_SERVER_PORT = ""
ENV BASE_WEBHOOK_URL = ""
ENV requests_main_url = ""
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r /requirements.txt

COPY . .

RUN py main.py
