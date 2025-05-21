from dispositivo_informatico import DispositivoInformatico
class Tableta(DispositivoInformatico):
    def __init__(self, marca: str) -> None:
        self.marca = marca
        
    def __str__(self) -> str:
        return f"Marca = {self.marca}"
