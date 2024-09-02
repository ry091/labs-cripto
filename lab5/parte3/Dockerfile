FROM ubuntu:22.10

COPY sources.list /etc/apt/sources.list

ENV DEBIAN_FRONTEND=noninteractive

# Actualizar los repositorios e instalar las dependencias necesarias
RUN apt-get update && \
    apt-get install -y build-essential wget zlib1g-dev libssl-dev sudo tshark

# Dar permisos a tshark
RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap

# Crear el usuario prueba con privilegios sudo
RUN useradd -m prueba && \
    echo 'prueba:prueba' | chpasswd

# Instalar OpenSSH Portable 9.0
RUN wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-9.0p1.tar.gz && \
    tar zxvf openssh-9.0p1.tar.gz

WORKDIR /openssh-9.0p1

# Crear el directorio /etc/ssh si no existe
RUN mkdir -p /etc/ssh

# Modificar el archivo sshd_config para reducir el tamaño del paquete de KEX
RUN echo "KexAlgorithms curve25519-sha256@libssh.org" > /etc/ssh/sshd_config && \
    echo "Ciphers aes128-ctr" >> /etc/ssh/sshd_config && \
    echo "MACs hmac-sha2-256" >> /etc/ssh/sshd_config

# Buildear desde source
RUN ./configure && \
    make && \
    make install

# Crear el usuario sshd para la separación de privilegios
RUN groupadd -r sshd && useradd -r -g sshd -d /var/empty -s /sbin/nologin -c "sshd Privilege Separation" sshd && \
    mkdir -p /var/run/sshd

# Crear el directorio /var/empty
RUN mkdir -p /var/empty

# Asegurarse de que el servicio SSH está configurado para iniciarse
RUN apt-get install -y openssh-server && \
    systemctl enable ssh

EXPOSE 22

# Iniciar el servidor SSH y mantener el contenedor activo
CMD ["/usr/sbin/sshd", "-D"]

