from Alarma import alarma
import random
class Sistema:
    def __init__(self):
        pass
    def Detectar(self):
        mov=random.choice([True,False])
        horario=random.choice([True,False])
        return mov,horario
    def Encender_Luces(self,mov,horario):
        Alarma=alarma()
        encender=Alarma.encender(mov,horario)
        print (encender)