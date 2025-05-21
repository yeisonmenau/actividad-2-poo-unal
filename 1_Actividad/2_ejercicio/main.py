from planeta import Planeta, TipoPlaneta
if __name__ == "__main__":
    planeta_uno = Planeta(TipoPlaneta.TERRESTRE, "Tierra", 1, 5.972e24, 1.08321e12, 12742, 150000000, True)
    planeta_uno.imprimir()
    print(f"Densidad del planeta: {planeta_uno.calcular_densidad()}")
    print(f"Es un planeta exterior: {planeta_uno.es_planeta_exterior()}\n")
    
    planeta_dos = Planeta(TipoPlaneta.GASEOSO, "Jupiter", 79, 1.899e27, 1.4313e15, 139820, 750000000, True)
    planeta_dos.imprimir()
    print(f"Densidad del planeta: {planeta_dos.calcular_densidad()}")
    print(f"Es un planeta exterior: {planeta_dos.es_planeta_exterior()}")