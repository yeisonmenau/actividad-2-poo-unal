from mascota import Mascota
from enum import Enum
class RazaPerroPequeño(Enum):
    CANICHE = "Caniche"
    YORKSHIRE_TERRIER = "Yorkshire Terrier"
    SCHNAUZER = "Schnauzer"
    CHIHUAHUA = "Chihuahua"

class RazaPerroMediano(Enum):
    COLLIE = "Collie"
    DALMATA = "Dálmata"
    BULLDOG = "Bulldog"
    GALGO = "Galgo"
    SABUESO = "Sabueso"

class RazaPerroGrande(Enum):
    PASTOR_ALEMAN = "Pastor Alemán"
    DOBERMAN = "Doberman"
    ROTWEILLER = "Rotweiller"
class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde
        
    def sonido():
        print("Los perros ladran")

class PerroPequeño(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: RazaPerroPequeño):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

class PerroMediano(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: RazaPerroMediano):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

class PerroGrande(Perro):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: RazaPerroGrande):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza