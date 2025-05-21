from mascota import Mascota
from enum import Enum

class RazaGatoSinPelo(Enum):
    ESFINGE = "Esfinge"
    ELFO = "Elfo"
    DONSKOY = "Donskoy"

class RazaGatoPeloLargo(Enum):
    ANGORA = "Angora"
    HIMALAYO = "Himalayo"
    BALINES = "Balinés"
    SOMALI = "Somalí"

class RazaGatoPeloCorto(Enum):
    AZUL_RUSO = "Azul Ruso"
    BRITANICO = "Británico"
    MANX = "Manx"
    DEVON_REX = "Devon Rex"

class Gato(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    def sonido():
        print("Los gatos maúllan y ronronean")
    

class GatoSinPelo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: RazaGatoSinPelo):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

class GatoPeloLargo(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: RazaGatoPeloLargo):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

class GatoPeloCorto(Gato):
    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: RazaGatoPeloCorto):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza