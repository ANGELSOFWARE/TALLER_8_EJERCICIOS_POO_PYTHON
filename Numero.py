class Numero:
    def __init__(self):
        self.dato_numero = ""
        
    def tomar_num(self):
        self.dato_numero = int(input("\nDigite un número: "))
        return self.dato_numero
        
    def mostrar_num(self):
        print(self.dato_numero)