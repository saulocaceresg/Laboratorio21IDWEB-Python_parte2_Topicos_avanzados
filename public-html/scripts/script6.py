# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0304, C0305, C0301, C0116
"""
8.	Crear una lista de diccionarios donde cada diccionario represente un equipo de fútbol, con las siguientes claves:
Nombre, país, nivelAtaque, nivelDefensa
Luego, convierte la lista completa a una cadena JSON y muéstrala en pantalla con formato legible.

"""
import json
print("====================== EJERCICIO 6 (8.) ======================")

# nivelAtaque -> [1 - 50]
# nivelDefensa -> [1 - 50]
lista_dic = [
    {"nombre": "Gutsfen", "pais": "Epeiror", "nivelAtaque": 33, "nivelDefensa": 25},
    {"nombre": "Redjudge", "pais": "Moscovia", "nivelAtaque": 41, "nivelDefensa": 32},
    {"nombre": "Centro 2B4", "pais": "Babilonia", "nivelAtaque": 25, "nivelDefensa": 42}
]

json_texto = json.dumps(lista_dic, indent=4)

print(json_texto)
print(type(json_texto))

print("==============================================================")
