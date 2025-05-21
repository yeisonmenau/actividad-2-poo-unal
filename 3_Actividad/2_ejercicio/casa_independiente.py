from casa_urbana import CasaUrbana
class CasaIndependiente(CasaUrbana):
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int, número_pisos: int, valor_area: int = 3000000):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos)

    def imprimir(self) -> None:
        super().imprimir()
        print()
