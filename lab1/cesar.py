def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():  # Verifica si el caracter es una letra
            # Convierte la letra a su posición en el alfabeto empezando desde 0 (A=0, B=1, ..., Z=25)
            posicion = ord(caracter.lower()) - ord('a') if caracter.islower() else ord(caracter) - ord('A')
            # Aplica el desplazamiento y calcula la nueva posición con módulo 26
            nueva_posicion = (posicion + desplazamiento) % 26
            # Convierte la nueva posición a la letra correspondiente
            nuevo_caracter = chr(nueva_posicion + ord('a')) if caracter.islower() else chr(nueva_posicion + ord('A'))
            resultado += nuevo_caracter
        else:
            # Si el caracter no es una letra, lo deja sin cambios
            resultado += caracter
    return resultado

# Solicitar al usuario que ingrese el texto a cifrar
texto = input("Texto a cifrar: ")

# Solicitar al usuario que ingrese el desplazamiento y convertirlo a entero
try:
    desplazamiento = int(input("Corrimiento: "))
    texto_cifrado = cifrado_cesar(texto, desplazamiento)
    print("Texto cifrado:", texto_cifrado)
except ValueError:
    print("El corrimiento debe ser un número entero.")

