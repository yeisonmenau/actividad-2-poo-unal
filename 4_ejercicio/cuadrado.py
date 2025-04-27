class Cuadrado:
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado 
    
    def calcular_perimetro(self) -> float:
        return 4 * self.lado