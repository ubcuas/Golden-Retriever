FROM python:3.7.4-buster

RUN pip3 install requests beautifulsoup4

COPY app.py .