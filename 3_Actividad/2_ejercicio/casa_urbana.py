from casa import Casa
class CasaUrbana(Casa):
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int, número_pisos: int):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos)

    def imprimir(self) -> None:
        super().imprimir()
