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