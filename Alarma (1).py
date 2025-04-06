class alarma:
    def __init__(self):
        self.encendido=True
    def encender(self,mov,horario):
        if horario==True and mov==True:
            return (f"\n¿Es de noche?: {horario}, ¿Hay movimiento en la habitación?: {mov}\n !LUCES ENCENDIDAS¡")
            
        else:
            return (f"\n¿Es de noche?: {horario}, ¿Hay movimiento en la habitación?: {mov}\n !LUCES APAGADAS¡")
            