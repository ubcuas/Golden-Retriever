FROM ubcuas/pyuuas:latest

RUN mkdir -p /uas/golden
WORKDIR /uas/golden

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY app.py ./
CMD ["python3", "app.py"]
