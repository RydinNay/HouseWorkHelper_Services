FROM python:3.10.0-alpine

WORKDIR /houshelper_services_api/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV BD ""

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r /requirements.txt

COPY . .
