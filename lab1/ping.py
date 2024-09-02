from scapy.all import ICMP, IP, send, Raw
from time import sleep, time


archivo_temporal = "id_icmp.txt"

# Función para leer el id_icmp desde un archivo temporal
def leer_id_icmp():
    try:
        with open(archivo_temporal, "r") as f:
            contenido = f.read().strip()
            # Verificar si el contenido es numérico y no está vacío
            if contenido.isdigit():
                return int(contenido)
            else:
                return 0
    except FileNotFoundError:
        return 0


# Función para guardar el id_icmp en un archivo temporal
def guardar_id_icmp(id_icmp):
    with open(archivo_temporal, "w") as f:
        f.write(str(id_icmp))

# Cargar el id_icmp al iniciar el script
id_icmp = leer_id_icmp()


def enviar_mensaje_oculto(mensaje, ip_destino='127.0.0.1'):
    global id_icmp
    seq_icmp = 1
    icmp_id = (0x0001 + id_icmp) & 0xffff
    payload_base = b'\x00' * 1+ b'\x01' *6+ b'\x00' * 5 + bytes(range(0x10, 0x38))

    for caracter in mensaje:
        if caracter == ' ':
            valor_caracter = 26
        elif caracter.isalpha():
            valor_caracter = ord(caracter.lower()) - ord('a')
        else:
            valor_caracter = 27

        timestamp_bytes = int(time()).to_bytes(4, 'big')
        valor_caracter_bytes = valor_caracter.to_bytes(1, 'little')

        payload_total = timestamp_bytes + payload_base + valor_caracter_bytes

        
        
        # Crear y enviar el paquete ICMP con el payload
        paquete = IP(dst=ip_destino)/ICMP(type="echo-request", id=icmp_id, seq=seq_icmp)/Raw(load=payload_total)
        send(paquete)
        seq_icmp += 1
        
        # Esperar 1 segundo entre cada envío para cumplir con el requisito de stealth
        sleep(1)
    
    id_icmp += 1
    guardar_id_icmp(id_icmp)

mensaje_a_enviar = input("Texto a enviar: ")
enviar_mensaje_oculto(mensaje_a_enviar)


