FROM python:3.12-slim

WORKDIR /app
COPY server.py /app/

RUN pip install --no-cache-dir requests

CMD ["python", "-u", "server.py"]