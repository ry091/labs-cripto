FROM ubuntu:22.10
ENV DEBIAN_FRONTEND=noninteractive
COPY sources.list /etc/apt/

RUN apt-get update && \
    echo "wireshark-common wireshark-common/install-setuid boolean false" | debconf-set-selections && \
    apt-get install -y build-essential zlib1g-dev libssl-dev libpam0g-dev libselinux1-dev wget tshark openssh-server

# Dar permisos a tshark
RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap

RUN useradd -m prueba && \
    echo 'prueba:prueba' | chpasswd

# Descargar el código fuente de OpenSSH
RUN wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-9.0p1.tar.gz && \
    tar -xzf openssh-9.0p1.tar.gz


RUN cd openssh-9.0p1 && \
    sed -i 's/^#define SSH_VERSION.*/#define SSH_VERSION "OpenSSH_?"/' version.h && \
    ./configure && \
    make && \
    make install

RUN apt-get install -y openssh-server

CMD ["/usr/sbin/sshd", "-D"]

