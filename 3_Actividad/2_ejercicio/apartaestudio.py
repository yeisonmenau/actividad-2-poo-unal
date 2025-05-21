from apartamento import Apartamento
class Apartaestudio(Apartamento):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int, valor_area: int = 1500000):
        super().__init__(identificador_inmobiliario, área, dirección, 1, 1)
        self._valor_area = valor_area

    def imprimir(self) -> None:
        super().imprimir()
        print()
