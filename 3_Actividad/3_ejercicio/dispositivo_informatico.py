class DispositivoInformatico:
    def __init__(self) -> None:
        self._marca: str = "Acer"
    
    def __str__(self) -> str:
        return f"Marca = {self._marca}"
