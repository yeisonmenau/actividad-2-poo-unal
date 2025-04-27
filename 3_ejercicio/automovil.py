from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = 1
    BIOETANOL = 2
    DIESEL = 3
    BIODIESEL = 4
    GAS_NATURAL = 5

class TipoAutomovil(Enum):
    CARRO_DE_CIUDAD = 1
    SUBCOMPACTO = 2
    COMPACTO = 3
    FAMILIAR = 4
    EJECUTIVO = 5
    SUV = 6

class Color(Enum):
    BLANCO = 1
    NEGRO = 2
    ROJO = 3
    NARANJA = 4
    AMARILLO = 5
    VERDE = 6
    AZUL = 7
    VIOLETA = 8
    
class Automovil:
    def __init__(self, marca: str, modelo: int, motor: float,  tipo_combustible: TipoCombustible, tipo_automovil: TipoAutomovil, numero_puertas: int, cantidad_asientos: int, velocidad_maxima: float, color: Color, velocidad_actual: float = 0):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual
     
    def acelerar(self, incremento_velocidad: float) -> None:
        if (self.velocidad_actual + incremento_velocidad) < self.velocidad_maxima:
               self.velocidad_actual += incremento_velocidad
        else:
            print("No se puede acelerar más allá de la velocidad máxima.")
            
    def desacelerar(self, decremento_velocidad: float) -> None:
        if (self.velocidad_actual - decremento_velocidad) > 0:
            self.velocidad_actual -= decremento_velocidad
        else:
            print("No se puede desacelerar a menos de 0 km/h.")
            
    def frenar(self) -> None:
        self.velocidad_actual = 0
    
    def calcular_tiempo_llegada(self, distancia: float) -> float:
        return distancia / self.velocidad_actual 
    
    def imprimir(self) -> None: 
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Tipo de Combustible: {self.tipo_combustible.name}")
        print(f"Tipo de Automóvil: {self.tipo_automovil.name}")
        print(f"Número de Puertas: {self.numero_puertas}")
        print(f"Cantidad de Asientos: {self.cantidad_asientos}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color.name}")    
        
    # Getters
    def get_marca(self) -> str:
        return self.marca

    def get_modelo(self) -> int:
        return self.modelo

    def get_motor(self) -> float:
        return self.motor

    def get_tipo_combustible(self) -> TipoCombustible:
        return self.tipo_combustible

    def get_tipo_automovil(self) -> TipoAutomovil:
        return self.tipo_automovil

    def get_numero_puertas(self) -> int:
        return self.numero_puertas

    def get_cantidad_asientos(self) -> int:
        return self.cantidad_asientos

    def get_velocidad_maxima(self) -> float:
        return self.velocidad_maxima

    def get_color(self) -> Color:
        return self.color

    def get_velocidad_actual(self) -> float:
        return self.velocidad_actual

    # Setters
    def set_marca(self, marca: str) -> None:
        self.marca = marca

    def set_modelo(self, modelo: int) -> None:
        self.modelo = modelo

    def set_motor(self, motor: float) -> None:
        self.motor = motor

    def set_tipo_combustible(self, tipo_combustible: TipoCombustible) -> None:
        self.tipo_combustible = tipo_combustible

    def set_tipo_automovil(self, tipo_automovil: TipoAutomovil) -> None:
        self.tipo_automovil = tipo_automovil

    def set_numero_puertas(self, numero_puertas: int) -> None:
        self.numero_puertas = numero_puertas

    def set_cantidad_asientos(self, cantidad_asientos: int) -> None:
        self.cantidad_asientos = cantidad_asientos

    def set_velocidad_maxima(self, velocidad_maxima: float) -> None:
        self.velocidad_maxima = velocidad_maxima

    def set_color(self, color: Color) -> None:
        self.color = color

    def set_velocidad_actual(self, velocidad_actual: float) -> None:
        self.velocidad_actual = velocidad_actual
        
        
    

        
        
    
        
    
        
