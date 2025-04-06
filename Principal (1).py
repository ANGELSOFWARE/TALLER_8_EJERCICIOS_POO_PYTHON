import time
from Sensor import Sensor
from Usuario import Usuario

usuario = Usuario()
while True:
    temperatura=usuario.ingresar_temperatura()
    sensor=Sensor(temperatura)
    estado=sensor.medir_temperatura(temperatura) 
    print(f"Estado: {estado}")
    opc=input("\nDesea continuar con el sensor? (s/n): ").lower()
    if opc!="s":
        print ("Su ejecucion ha finalizado!")
        break
    time.sleep(5)