
class Usuario:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.asientos_reservar = 0
    
    def tomar_datos(self):
        self.nombre = input("\nIngrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
    def tomar_reserva(self):
        while True:
            try:
                self.asientos_reservar = int(input("\nIngrese la cantidad de asientos que desea reservar: "))
                if self.asientos_reservar >= 0:
                    break
                else:
                    print("\nPor favor, ingrese un número válido de asientos.")
            except ValueError:
                print("\nError: Ingrese un número válido.")

    def obtener_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
