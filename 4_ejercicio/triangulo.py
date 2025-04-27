class Triangulo:
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura
        
    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self) -> float:
        return self.base * 3
    
    def calcular_hipotenusa(self) -> float:
        return (self.base ** 2 + self.altura ** 2) ** 0.5
    
    def determinar_tipo(self) -> str:
        if self.base == self.altura and self.base == self.calcular_hipotenusa() and self.altura == self.calcular_hipotenusa():
            return "Equilátero"
        elif self.base != self.altura and self.base != self.calcular_hipotenusa() and self.altura != self.calcular_hipotenusa():
            return "Escaleno"
        else:
            return "Isósceles"