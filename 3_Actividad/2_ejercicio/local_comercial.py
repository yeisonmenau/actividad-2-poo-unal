from local import Local
class LocalComercial(Local):
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, tipo_local: Local.Tipo, centro_comercial: str, valor_area: int = 3000000):
        super().__init__(identificador_inmobiliario, área, dirección, tipo_local)
        self.centro_comercial = centro_comercial

    def imprimir(self) -> None:
        super().imprimir()
        print(f"Centro comercial = {self.centro_comercial}")
