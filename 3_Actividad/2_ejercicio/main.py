from apartamento_familiar import ApartamentoFamiliar
from apartaestudio import Apartaestudio

apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
print("Datos apartamento")
apto1.calcular_precio_venta() 
apto1.imprimir()

print("Datos apartamento")
aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1)
aptestudio1.calcular_precio_venta()
aptestudio1.imprimir()
