from Sistema_aire import Sistema_aire
from Usuario import Usuario
import time 
usuario = Usuario()
sistema = Sistema_aire()

while True: 
    temp, humedad = usuario.ingresar_datos()
    sistema.Encender_aire(temp, humedad)
    time.sleep(3)
     
    if not usuario.continuar():
        break