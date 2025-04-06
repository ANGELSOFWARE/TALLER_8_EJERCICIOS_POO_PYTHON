from Usuario import Usuario 

class Calculadora:
    def __init__(self):
        pass

    def calcular(self, usuario):
        if usuario.operacion == "+":
            resultado = usuario.numero1 + usuario.numero2
        elif usuario.operacion == "-":
            resultado = usuario.numero1 - usuario.numero2
        elif usuario.operacion == "*":
            resultado = usuario.numero1 * usuario.numero2
        elif usuario.operacion == "/":
            if usuario.numero2 == 0:
                return "\nError: No se puede dividir por cero."
            resultado = usuario.numero1 / usuario.numero2
        
        return f"\nResultado: {usuario.numero1} {usuario.operacion} {usuario.numero2} = {resultado:.2f}"

        
        
                    
        
        