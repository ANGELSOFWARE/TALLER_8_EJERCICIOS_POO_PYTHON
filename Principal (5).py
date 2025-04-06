from Tienda import SistemaAcceso 
from Usuario import Usuario  
import time  

sistema = SistemaAcceso()  

while True:
    usuario = Usuario()  
    usuario.tomar_datos()  
    sistema.validar_entrada(usuario) 
    time.sleep(3) 
