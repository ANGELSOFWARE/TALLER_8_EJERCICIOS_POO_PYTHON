from UsuariosCine import Usuario
from salacine import Sala

sala = Sala()
usuario = Usuario()
usuario.tomar_datos()
while not sala.sala_llena():
    usuario.tomar_reserva()

    if sala.reservar_asientos(usuario.asientos_reservar):
        print(f"\n¡Gracias, {usuario.obtener_nombre_completo()}! Su reserva ha sido confirmada.")
        
    if sala.sala_llena():
        print("\nLa sala está llena. No se pueden hacer más reservas.")
        break

    continuar = input("\n¿Desea hacer otra reserva? (s/n): ").strip().lower()
    if continuar != "s":
        print("\nFinalizando el sistema de reservas. ¡Hasta luego!")
        break

