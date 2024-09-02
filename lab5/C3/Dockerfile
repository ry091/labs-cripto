FROM ubuntu:20.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|http://old-releases.ubuntu.com/ubuntu/|g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu groovy main multiverse restricted universe" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu groovy-backports main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu groovy-proposed main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu groovy-security main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu groovy-updates main multiverse restricted universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y sudo net-tools libedit2 openssh-client openssh-server tshark

# Mantener el contenedor activo
CMD ["tail", "-f", "/dev/null"]

