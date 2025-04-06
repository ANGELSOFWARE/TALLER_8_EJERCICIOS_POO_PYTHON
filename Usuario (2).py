class Usuario:
    def __init__(self):
        pass
    def ingresar_datos(self):
        try:
            temp=float(input("\nIngrese la temperatura actual de su invernadero: "))
            humedad=float(input("Ingrese el porcentaje actual de la humedad de su invernadero: "))
            return temp,humedad
        except ValueError:
            print("\nERROR, Ingrese un dato valido")
            
    def continuar(self):
        while True:
            opc = input("\nDesea continuar en el sistema?(s/n): ").strip().lower()
            if opc=="s":
                return True
            elif opc == "n":
                print("\nLa ejecución del sistema ha finalizado.")
                return False
            else:
                print("\nOpción no válida, ingrese 's' para sí o 'n' para no.")