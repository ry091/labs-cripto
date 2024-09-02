


from scapy.all import rdpcap, Raw
from colorama import Fore, Style, init

# Inicializa colorama
init(autoreset=True)

def decodificar_cesar(texto, desplazamiento):
    decodificado = ''
    for char in texto:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            decodificado += chr((ord(char) - offset - desplazamiento) % 26 + offset)
        else:
            decodificado += char
    return decodificado

def leer_mensaje_de_pcap(archivo_pcap):
    paquetes = rdpcap(archivo_pcap)
    mensaje_codificado = ''
    for paquete in paquetes:
        if paquete.haslayer(Raw):
            datos = paquete[Raw].load
            valor_caracter = datos[-1]
            if 0 <= valor_caracter <= 25:
                mensaje_codificado += chr(valor_caracter + ord('a'))
            elif valor_caracter == 26:
                mensaje_codificado += ' '
    return mensaje_codificado

def intentar_todas_rotaciones(texto_codificado):
    resultados = []
    for i in range(26):
        resultados.append((i, decodificar_cesar(texto_codificado, i)))
    return resultados

def puntuacion_legibilidad(mensaje):
    secuencias_comunes = [
        'de', 'la', 'que', 'el', 'en', 'los', 'con', 'las', 'un', 'por', 'para', 'es',
        'al', 'se', 'del', 'lo', 'como', 'mas', 'su', 'le', 'si', 'mi', 'me', 'esta',
        'ya', 'que', 'por', 'su', 'al', 'lo', 'le', 'se'
    ]
    puntuacion = 0
    mensaje = mensaje.lower()
    for secuencia in secuencias_comunes:
        puntuacion += mensaje.count(secuencia)
    return puntuacion

def resaltar_mejor_opcion(resultados):
    mejor_puntuacion = -1
    mejor_mensaje = ''
    rotacion_probable = 0

    # Determinar la opción más probable
    for rotacion, mensaje in resultados:
        puntuacion_actual = puntuacion_legibilidad(mensaje)
        if puntuacion_actual > mejor_puntuacion:
            mejor_puntuacion = puntuacion_actual
            mejor_mensaje = mensaje
            rotacion_probable = rotacion

    # Imprimir resultados, destacando el más probable en verde
    for rotacion, mensaje in resultados:
        if rotacion == rotacion_probable:
            print(Fore.GREEN + f"Rotación {rotacion}: {mensaje}")
        else:
            print(f"Rotación {rotacion}: {mensaje}")

archivo_pcap = input("Ingrese la ruta al archivo pcap: ")
mensaje_codificado = leer_mensaje_de_pcap(archivo_pcap)
print("Mensaje codificado:", mensaje_codificado)

resultados = intentar_todas_rotaciones(mensaje_codificado)
resaltar_mejor_opcion(resultados)
