from casa_urbana import CasaUrbana
class CasaConjuntoCerrado(CasaUrbana):
    valor_area = 2500000

    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, número_habitaciones: int, número_baños: int, número_pisos: int, valor_administración: int, tiene_piscina: bool, tiene_campos_deportivos: bool, valor_area: int = 2500000):
        super().__init__(identificador_inmobiliario, área, dirección, número_habitaciones, número_baños, número_pisos)
        self._valor_administración = valor_administración
        self._tiene_piscina = tiene_piscina
        self._tiene_campos_deportivos = tiene_campos_deportivos
        self._valor_area = valor_area

    def imprimir(self) -> None:
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administración}")
        print(f"Tiene piscina? = {self._tiene_piscina}")
        print(f"Tiene campos deportivos? = {self._tiene_campos_deportivos}")
        print()
