class Sala:
    def __init__(self, capacidad_total=50):
        self.capacidad_disponible = capacidad_total 
    
    def verificar_disponibilidad(self, cantidad):
        return cantidad <= self.capacidad_disponible  
    
    def reservar_asientos(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.capacidad_disponible -= cantidad  
            print(f"\nReserva exitosa!.")
            print(f"\nAsientos disponibles: {self.capacidad_disponible}")
            return True
        else:
            print(f"\nNo hay suficientes asientos disponibles. Solo quedan {self.capacidad_disponible}.")
            return False
    
    def sala_llena(self):
        return self.capacidad_disponible == 0  
        