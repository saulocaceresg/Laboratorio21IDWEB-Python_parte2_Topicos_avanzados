# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0304, C0305, C0301, C0116
"""
7.	Crear un programa que permita Copiar el contenido de un archivo a otro. 2 versiones: una para archivos de texto y otra para archivos binarios
"""
# import shutil
print("====================== EJERCICIO 4 (6.) ======================")

# Función para copiar archivo de texto
def copiar_archivo(ruta):
    with open(f"{ruta}/archivo.txt", "r", encoding="utf-8") as origen:
        with open(f"{ruta}/archivo_copia.txt", "w", encoding="utf-8") as copia:
            for linea in origen:
                copia.write(linea)
    
    print("Se ha copiado el archivo")

# Función para copiar archivo binario (imagen)
def copiar_archivo_binario(ruta):
    with open(f"{ruta}/imagen.jpg", "rb") as bin_origen:
        with open(f"{ruta}/copia_imagen.png", "wb") as bin_copia:
            bin_copia.write(bin_origen.read())
    
    print("Se ha copiado el archivo binario")


destino = "public-html/recursos"

# Se crea manualmente el archivo.txt
with open(f"{destino}/archivo.txt", "w", encoding="utf-8") as f:
    f.write("Hola mundo\nEste es un archivo de texto. :D\n")

copiar_archivo(destino)

# El archivo binario ya se agregó antes (imagen.jpg)
copiar_archivo_binario(destino)

print("==============================================================")
