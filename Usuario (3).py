class Usuario:
    def __init__(self):
        self.nombre = ""
        self.membresia = ""
        self.empleado = ""

    def tomar_datos(self):
        self.nombre = input("\n¿Cuál es tu nombre?: ").capitalize()
        self.membresia = input("¿Tienes membresía? (si/no): ").strip().lower()
        self.empleado = input("¿Eres empleado? (si/no): ").strip().lower()
