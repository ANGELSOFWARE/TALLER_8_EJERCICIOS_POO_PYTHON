class Usuario:
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.operacion = ""

    def solicitar_datos(self):
        while True:
            try:
                self.numero1 = float(input("\nIngrese el primer número: "))
                self.numero2 = float(input("Ingrese el segundo número: "))
                break
            except ValueError:
                print("Error: Debe ingresar valores numéricos.")

        while True:
            self.operacion = input("Ingrese la operación (+, -, *, /): ").strip()
            if self.operacion in ["+", "-", "*", "/"]:
                break
            else:
                print("Error: Operación inválida. Intente nuevamente.")

        return self.numero1, self.numero2, self.operacion
