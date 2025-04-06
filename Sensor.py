from Usuario import Usuario
class Sensor:
    def __init__(self,temperatura):
        self.temperatura=temperatura
    def medir_temperatura(self,temperatura):
        if temperatura<10:
            return "CALEFACTOR ACTIVADO"
        elif temperatura>=10 and temperatura<25:
            return "Temperatura de invernadero ESTABLE"
        elif temperatura>=25:
            return "VENTILADOR ACTIVADO"
        

    