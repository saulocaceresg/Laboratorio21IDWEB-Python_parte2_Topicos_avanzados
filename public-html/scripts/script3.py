# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0303, C0304, C0305, C0301, C0116
"""
5.	Leer la operación como un solo string
Ejemplo: "10 / 2"
Separar los componentes y validar:
•	numero1 y numero2 deben poder convertirse a float
•	operador debe ser uno de: + - * / 
Realizar la operación, pero manejar las excepciones:
•	División entre cero → mostrar mensaje personalizado
•	Valores inválidos → manejar ValueError
•	Operador inválido → lanzar una excepción personalizada (crear clase que herede de Exception)

"""
print("====================== EJERCICIO 3(5.) ======================")

class OperadorInvalido(Exception):
    """ Clase que hereda de Exception """
    pass

class Operador:
    """ Clase operador para imprimir error """
    def __init__(self, operador):
        self.operador = operador
        self.validar_operador()
    
    def validar_operador(self):
        validos = ('+', '-', '*', '/')

        if self.operador not in validos:
            raise OperadorInvalido(f"OPERADOR NO VÁLIDO: {self.operador}")
    
try:
    operacion = "10 / 0"
    componentes = []
    cadena = ""
    for i in operacion:
        if i == " ":
            componentes.append(cadena)
            cadena = ""
            continue

        cadena += i

    if cadena:
        componentes.append(cadena)

    numero1 = float(componentes[0])
    numero2 = float(componentes[2])

    if numero2 == 0:
        raise ZeroDivisionError("NO SE PUEDE DIVIDIR POR CERO")

    print(componentes)

    op = Operador(componentes[1])
    print("OPERADOR CORRECTO")

except ZeroDivisionError:
    print("NO SE PUEDE DIVIDIR ENTRE CERO")
except ValueError:
    print("VALORES NO VÁLIDOS")
except OperadorInvalido as e:
    print(e)


print("=============================================================")
