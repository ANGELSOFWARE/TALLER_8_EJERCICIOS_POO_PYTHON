from Detector import Detector

class Alarma:
    def __init__(self):
        pass 
    def Activar_automatico(self,mov1,mov2,mov3,noche):
        if (noche==True and mov1==True and mov2==True) or\
        (noche==True and mov2==True and mov3==True) or\
        (noche==True and mov1==True and mov3==True):
            print(f"\n¿Es de noche?: {'Si'if noche else 'No'}, ¿Hay movimiento detectado?: Sensor 1: {'Si'if mov1 else 'No'},Sensor 2: {'Si'if mov2 else 'No'}, Sensor 3;{'Si'if mov3 else 'No'}")
            print("¡ALARMA ACTIVADA!\n")
        else:
            print(f"\n¿Es de noche?: {'Si'if noche else 'No'}, ¿Hay movimiento detectado?: Sensor 1: {'Si'if mov1 else 'No'}, Sensor 2: {'Si'if mov2 else 'No'}, Sensor 3;{'Si'if mov3 else 'No'}")
            print("¡ALARMA DESACTIVADA!\n")
    def Activar_manual(self):
            print("\nPulsa 1 para activar la alarma")
            print("Pulsa 2 para desactivarla")
            opc=int(input("Digite su opción: "))
            if opc==1:
                print("ALARMA ACTIVADA")
            elif opc==2:
                print("ALARMA ACTIVADA")
            else:
                print("Digite una opción valida: ")