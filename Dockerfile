FROM python:3.6-alpine3.8

MAINTAINER Dmytro Frolov: version 0.1

EXPOSE 6105

ENV PORT 6105

COPY . /app

WORKDIR /app

CMD ["python3", "udp_server.py"]
