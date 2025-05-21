from inmueble_vivienda import InmuebleVivienda
class Casa(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int, número_pisos: int):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños)
        self._número_pisos = número_pisos

    def imprimir(self)-> None:
        super().imprimir()
        print(f"Número de pisos = {self._número_pisos}")
