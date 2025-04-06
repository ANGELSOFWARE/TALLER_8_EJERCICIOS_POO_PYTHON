from Alarma import alarma
from Sistema import Sistema
import time 
sistema=Sistema()
Alarma=alarma()
while True:
    mov,horario=sistema.Detectar()
    Alarma.encender(mov,horario)
    sistema.Encender_Luces(mov,horario)
    opc=input("\n¿Desea Continuar en el sistema? (s/n): ").strip().lower()
    if opc!="s":
        print("\nLa ejecución del sistema ha finalizado")
        break
    time.sleep(3)