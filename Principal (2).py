from Detector import Detector
from Alarma import Alarma
import time
detector=Detector()
alarma=Alarma()
while True:
    try:
        alarma.Activar_manual()
        mov1,mov2,mov3,noche=detector.detectar_datos()
        alarma.Activar_automatico(mov1,mov2,mov3,noche)
        opc2=input("¿Deseas continuar? (s/n): ").lower()
        if opc2!="s":
            print("El detector ha finalizado su ejecución")
            break
        time.sleep(3)
    except ValueError:
        print("Ingrese una nopción valida")