FROM ubuntu:16.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|http://old-releases.ubuntu.com/ubuntu/|g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu yakkety main multiverse restricted universe" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu yakkety-backports main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu yakkety-proposed main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu yakkety-security main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu yakkety-updates main multiverse restricted universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y sudo net-tools libedit2 openssh-client openssh-server tshark


CMD ["tail", "-f", "/dev/null"]

