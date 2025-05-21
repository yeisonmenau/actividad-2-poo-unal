from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado
from triangulo import Triangulo

def Main():
    circulo = Circulo(2)
    rectangulo = Rectangulo(1, 2)
    cuadrado = Cuadrado(3)
    triangulo = Triangulo(3, 4)
    
    print(f"El area del circulo es: {circulo.calcular_area()}")
    print(f"El perimetro del circulo es: {circulo.calcular_perimetro()}\n")
    
    print(f"El area del rectangulo es: {rectangulo.calcular_area()}")
    print(f"El perimetro del rectangulo es: {rectangulo.calcular_perimetro()}\n")
    
    print(f"El area del cuadrado es: {cuadrado.calcular_area()}")
    print(f"El perimetro del cuadrado es: {cuadrado.calcular_perimetro()}\n")
    
    print(f"El area del triangulo es: {triangulo.calcular_area()}")
    print(f"El perimetro del triangulo es: {triangulo.calcular_perimetro()}")
    print(f"Tpo de triangulo: {triangulo.determinar_tipo()}")
    

if __name__  == "__main__":
    Main()