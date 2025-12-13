# (IGNORAR) Para que no subraye errores pequeños e irrelevantes de sintaxis
# pylint: disable=C0103, C0114, C0304, C0305, C0301, C0116
"""
3.	Usando una jerarquía de clases que permita calcular el área y el perímetro de Rectángulo, Triángulo y Círculo. Crear una lista con un objeto de cada figura y mostrar sus datos
"""
print("====================== EJERCICIO 1(3.) ======================")

class Figura:
    """
    Clase padre Figura
    """
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return self.lado1 * self.lado2

    def mostrar_datos(self):
        return f"Lado 1: {self.lado1}\nLado 2: {self.lado2}\nÁrea: {self.area()}"

class Rectangulo(Figura):
    """
    Clase hija Rectángulo
    """
    def perimetro(self):
        return self.lado1 * 2 + self.lado2 * 2

    def mostrar_datos(self):
        return "---- Rectángulo ----\n" + super().mostrar_datos() + f"\nPérímetro: {self.perimetro()}"

class Triangulo(Figura):
    """
    Clase hija Triangulo
    """
    def __init__(self, lado1, lado2, lado3):
        super().__init__(lado1, lado2)
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        # Se usa la fórmula de Herón
        semiperimetro = self.perimetro() / 2
        area_T = (semiperimetro * (semiperimetro - self.lado1) * (semiperimetro - self.lado2) * (semiperimetro - self.lado3)) ** (0.5)
        return area_T

    def mostrar_datos(self):
        return f"---- Triángulo ----\nLado 1: {self.lado1}\nLado 2: {self.lado2}\nLado 3: {self.lado3}\nÁrea: {self.area()}\nPerímetro: {self.perimetro()}"

class Circulo(Figura):
    """
    Clase hija Círculo
    """
    def __init__(self, lado1, lado2 = 3.141592):
        # lado1 es radio, lado2 es PI
        super().__init__(lado1, lado2)

    def perimetro(self):
        return 2 * self.lado2 * self.lado1

    def mostrar_datos(self):
        return f"---- Círculo ----\nRadio: {self.lado1}\nPI: {self.lado2}\nÁrea: {self.area() ** 2}\nPerímetro: {self.perimetro()}"

# =============== PARTE PRINCIPAL =================
# Entrada de datos
lista_figuras = [Rectangulo(4, 9), Triangulo(3, 5, 4), Circulo(8)]

for i in lista_figuras:
    print(i.mostrar_datos())


print("=============================================================")
