from Numero import Numero
class Juego:
    def __init__(self):
        self.objnum = Numero()
        
    def tomar_dato(self):
        numero = self.objnum.tomar_num() 
        return numero
        
    def operar(self, numero):
        res1 = numero % 3
        res2 = numero % 5
        if res1 == 0 and res2 == 0:
            print("FizzBuzz")
        elif res1 == 0 and res2 != 0:
            print("Fizz")
        elif res1 != 0 and res2 == 0:
            print("Buzz")
        else:
            print(numero)
    def mostrar(self):
        while True:
            opc = self.continuar()
            if opc==1:
                numero=self.tomar_dato()
                self.operar(numero)
            else:
                print("Su ejecución ha finalizado")
                break
    def continuar(self):
        try:
            print("\nPulsa 1 para permanecer en el juego")
            print("Pulsa 2 para salir del sistema")
            opc=int(input("Digite su opción: "))
            return opc
        except ValueError:
            print("\nDigite una opción Valida: ")
            return self.continuar()