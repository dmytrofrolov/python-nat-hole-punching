FROM ubuntu:16.04

MAINTAINER Dmytro Frolov: version 0.1

EXPOSE 6104

COPY start.sh /start.sh

CMD ["bash", "start.sh"]
