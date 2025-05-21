from apartamento import Apartamento
class ApartamentoFamiliar(Apartamento):
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int, valor_administración: int, valor_area: int = 2000000):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños)
        self._valor_administración = valor_administración
        self._valor_area = valor_area

    def imprimir(self) -> None:
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administración}")
        print()
