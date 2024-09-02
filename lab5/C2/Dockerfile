FROM ubuntu:18.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/archive.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu cosmic main multiverse restricted universe" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu cosmic-backports main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu cosmic-proposed main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu cosmic-security main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu cosmic-updates main multiverse restricted universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y sudo net-tools libedit2 openssh-client openssh-server tshark

# Mantener el contenedor activo
CMD ["tail", "-f", "/dev/null"]

