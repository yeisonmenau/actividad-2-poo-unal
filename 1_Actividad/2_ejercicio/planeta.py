from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3

class Planeta:
    def __init__(self,  tipo_planeta: TipoPlaneta, nombre: str = None, cantidad_satelites: int = 0, masa: float = 0, volumen: float = 0, diametro: float = 0, distancia_sol: float = 0, observable: bool = False):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo_planeta = tipo_planeta
        self.observable = observable
        
    def imprimir(self) -> None:
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de satelites: {self.cantidad_satelites}")
        print(f"Masa: {self.masa} kg")
        print(f"Volumen: {self.volumen} km cubicos")
        print(f"Diametro: {self.diametro} km")
        print(f"Distancia al sol: {self.distancia_sol} km")
        print(f"Tipo de planeta: {self.tipo_planeta.name}")
    
    def calcular_densidad(self) -> float:
        return self.masa / self.volumen
    
    def es_planeta_exterior(self) -> bool:
        limite = (149597870 * 3.4)
        if self.distancia_sol > limite:
            return True
        return False