from inmueble import Inmueble
class InmuebleVivienda(Inmueble):
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int):
        super().__init__(identificador_inmobiliario, área, dirección)
        self._número_habitaciones = número_habitaciones
        self._número_baños = número_baños

    def imprimir(self)-> None:
        super().imprimir()
        print(f"Número de habitaciones = {self._número_habitaciones}")
        print(f"Número de baños = {self._número_baños}")
