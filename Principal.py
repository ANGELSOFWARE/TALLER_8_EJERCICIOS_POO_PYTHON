from Calculadora import Calculadora
from Usuario import Usuario

calculadora = Calculadora()

while True:
    usuario = Usuario() 
    usuario.solicitar_datos() 

    resultado = calculadora.calcular(usuario) 
    print(resultado) 
    continuar = input("\n¿Desea realizar otro cálculo? (s/n): ").strip().lower()
    if continuar != "s":
        print("Gracias por usar la calculadora. ¡Hasta pronto!")
        break 

