class Sistema_aire:
    def __init__(self):
        self.aire=""
    def Encender_aire(self,temp,humedad):
        if (temp>28 and humedad>60) or temp>30:
            print(f"\nEstado: AIRE ACONDICIONADO ENCENDIDO")
        else:
            print (f"\nEstado: AIRE ACONDICIONADO APAGADO")