FROM python:3.8.3-slim

COPY requirements.txt /tmp/
WORKDIR /app
COPY app.py /app/
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
CMD ["python", "/app/app.py"]