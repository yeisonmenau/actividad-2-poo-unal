from math import pi

class Circulo:
    def __init__(self, radio: float) -> None:
        self.radio = radio
        
    def calcular_area(self) -> float:
        return pi * self.radio ** 2
    
    def calcular_perimetro(self) -> float:
        return 2 * pi * self.radio    
    