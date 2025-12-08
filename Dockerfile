FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN mkdir -p /app/stories

EXPOSE 8080

LABEL author="Márton Áron"