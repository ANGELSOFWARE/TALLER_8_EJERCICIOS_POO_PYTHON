class Usuario:
    def __init__(self):
        pass
    def ingresar_temperatura(self):
        while True:
            try:
                return int(input("\nDigite la temperatura actual de su invernadero: "))
            except ValueError:
                print("\nError: Por favor, ingrese un número válido.")

    
        
        