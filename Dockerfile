FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y git

RUN apt-get update \
    && apt-get install -y python3

MAINTAINER Dmytro Frolov: version 0.1

EXPOSE 6104

COPY start.sh /start.sh

CMD ["bash", "start.sh"]
