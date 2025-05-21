from perro import Perro, PerroPequeño, RazaPerroPequeño
from gato import Gato, GatoPeloLargo, RazaGatoPeloLargo

perrito = PerroPequeño("Fido", 3, "Marrón", 5.2, True, RazaPerroPequeño.CANICHE)
Perro.sonido()

gatito = GatoPeloLargo("Misu", 2, "Blanco", 0.8, 1.5, RazaGatoPeloLargo.ANGORA)
Gato.sonido()