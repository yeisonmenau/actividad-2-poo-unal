from casa import Casa
class CasaRural(Casa):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int, número_pisos: int, distancia_cabera: int, altitud: int):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos)
        self._distancia_cabera = distancia_cabera
        self._altitud = altitud

    def imprimir(self)-> None:
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self._distancia_cabera} km.")
        print(f"Altitud sobre el nivel del mar = {self._altitud} metros.")
        print()
