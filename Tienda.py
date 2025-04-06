from datetime import datetime
from Usuario import Usuario 

class SistemaAcceso:
    def __init__(self):
        self.horario_atencion = (7, 20)  

    def dentro_horario(self):
        hora_actual = datetime.now().hour
        return self.horario_atencion[0] <= hora_actual < self.horario_atencion[1]

    def validar_entrada(self, usuario):
        horario = self.dentro_horario()
        if usuario.membresia == "si" and horario or usuario.empleado == "si":
            print(f"ACCESO PERMITIDO. ¡Bienvenid@ {usuario.nombre}!")
        else:
            print(f"ACCESO DENEGADO. Lo sentimos {usuario.nombre}.")
