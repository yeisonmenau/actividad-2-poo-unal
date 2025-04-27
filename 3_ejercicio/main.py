from automovil import Automovil, TipoCombustible, TipoAutomovil, Color

if __name__ == "__main__":
    automovil_uno = Automovil("Ford", 2018, 3, TipoCombustible.DIESEL, TipoAutomovil.EJECUTIVO, 4,6,250, Color.NEGRO)
    automovil_uno.imprimir()
    automovil_uno.set_velocidad_actual(100)
    print(f"Velocidad actual: {automovil_uno.velocidad_actual}")
    automovil_uno.acelerar(20)
    print(f"Velocidad actual: {automovil_uno.velocidad_actual}")
    automovil_uno.desacelerar(50)
    print(f"Velocidad actual: {automovil_uno.velocidad_actual}")
    automovil_uno.frenar()
    print(f"Velocidad actual: {automovil_uno.velocidad_actual}")
    automovil_uno.desacelerar(20)
    
    