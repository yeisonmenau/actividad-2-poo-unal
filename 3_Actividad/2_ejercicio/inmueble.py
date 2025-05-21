class Inmueble:
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str):
        self._identificador_inmobiliario = identificador_inmobiliario
        self._área = área
        self._dirección = dirección
        self.precio_venta = 0.0

    def calcular_precio_venta(self, valor_area: float) -> float:
        self._precio_venta = self._área * valor_area
        return self._precio_venta

    def imprimir(self)-> None:
        print(f"Identificador inmobiliario = {self._identificador_inmobiliario}")
        print(f"Área = {self._área}")
        print(f"Dirección = {self._dirección}")
        print(f"Precio de venta = ${self._precio_venta}")

