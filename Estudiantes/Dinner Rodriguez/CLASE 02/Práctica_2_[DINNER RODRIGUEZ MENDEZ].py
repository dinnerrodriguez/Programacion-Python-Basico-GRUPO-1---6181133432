"""
PRACTICA 2:

"""
numeros = [1,2,3,4,5,6,7,8,9,10]
extension = (11,12,13,14,15)
print(numeros)

numeros.extend(extension)
print (numeros)

numeros.append(16)
print (numeros)

numeros.insert(0,0)
print(numeros)

numeros.remove(5)
print(numeros)

numeros.pop(-1)
print(numeros)

ultimo_numero = numeros.pop()
print(ultimo_numero)
print(numeros)


# Crear un archivo en modo escritura
# Especificar la ruta completa donde quieres guardar el archivo

import os

# Obtener la ruta de la carpeta Descargas del usuario
ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads", "numeros.txt")


# Crear el archivo en modo escritura y escribir los números en líneas separadas
with open(ruta_descargas, "w") as archivo:
    for numero in numeros:
        archivo.write(f"{numero}\n")  # Escribe cada número en una nueva línea

# Cerrar el archivo con el método close()
archivo.close()

print(f"Archivo creado en: {ruta_descargas}")

"""
CON AYUDA DE CHAT GPT:

os.path.expanduser("~") obtiene la ruta del usuario.

os.path.join(...) combina la ruta de Descargas con el nombre del archivo.

open(..., "w") abre el archivo en modo escritura, creando o sobrescribiendo su contenido.

"""


# Ruta del archivo (debe existir previamente)

ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads", "numeros.txt")

# Abrir el archivo en modo lectura
archivo = open(ruta_descargas, "r")

# Leer todo el contenido del archivo
contenido = archivo.read()

# Mostrar el contenido
print(contenido)

# Cerrar el archivo
archivo.close()
