FROM python:alpine3.8
ADD . /app

RUN pip install prometheus_client

CMD [ "python", "/app/server.py" ]