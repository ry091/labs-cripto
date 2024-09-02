FROM ubuntu:22.10
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|http://old-releases.ubuntu.com/ubuntu/|g' /etc/apt/sources.list

RUN echo "deb http://old-releases.ubuntu.com/ubuntu kinetic main multiverse restricted universe" > /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu kinetic-backports main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu kinetic-proposed main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu kinetic-security main multiverse restricted universe" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu kinetic-updates main multiverse restricted universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y sudo net-tools libedit2 openssh-client openssh-server tshark

# Crear usuario prueba con contraseña prueba
RUN useradd -m prueba && \
    echo 'prueba:prueba' | chpasswd


EXPOSE 22

# Iniciar el servidor SSH
CMD ["/usr/sbin/sshd", "-D"]

