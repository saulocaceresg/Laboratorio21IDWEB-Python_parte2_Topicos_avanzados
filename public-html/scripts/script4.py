"""
6.	Crear un módulo geometria.py con lo hecho en el ejercicio 3 y utilizarlo desde otro archivo
"""
import geometria
print("====================== EJERCICIO 4 (6.) ======================")

try:
    operador = geometria.Operador("p")

    print("OPERADOR CORRECTO")
    
except geometria.OperadorInvalido as e:
    print(e)


print("==============================================================")
