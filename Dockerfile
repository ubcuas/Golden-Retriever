FROM python:3.7.4-buster

RUN mkdir -p /uas/gcomx/golden
WORKDIR /uas/gcomx/golden

RUN pip3 install requests beautifulsoup4

COPY app.py .