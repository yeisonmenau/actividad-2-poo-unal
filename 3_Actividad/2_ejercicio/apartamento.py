from inmueble_vivienda import InmuebleVivienda
class Apartamento(InmuebleVivienda):
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños)

    def imprimir(self)-> None:
        super().imprimir()
