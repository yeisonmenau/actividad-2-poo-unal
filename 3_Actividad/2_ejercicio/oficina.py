from local import Local
class Oficina(Local):
    def __init__(self, identificador_inmobiliario: int, área: int, dirección: str, tipo_local: Local.Tipo, es_gobierno: bool, valor_area: int = 3500000):
        super().__init__(identificador_inmobiliario, área, dirección, tipo_local)
        self.es_gobierno = es_gobierno

    def imprimir(self) -> None:
        super().imprimir()
        print(f"Es oficina gubernamental = {self.es_gobierno}")
