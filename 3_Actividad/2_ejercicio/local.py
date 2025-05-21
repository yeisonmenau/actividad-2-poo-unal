from inmueble import Inmueble
from enum import Enum

class Local(Inmueble):
    class Tipo(Enum):
        INTERNO = 1
        CALLE = 2

    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, tipo_local: Tipo):
        super().__init__(identificador_inmobiliario, área, dirección)
        self.tipo_local = tipo_local

    def imprimir(self) -> None:
        super().imprimir()
        print(f"Tipo de local = {self.tipo_local.name}")
