from estudiante import Estudiante
from profesor import Profesor

estudiante1 = Estudiante("Juan", "Calle Falsa 123", "Ingeniería", 3)
profesor1 = Profesor("Profe", "Calle Falsa 456", "Matemáticas", "Titular")
print(estudiante1.getNombre())
print(estudiante1.setCarrera("Medicina"))

print(profesor1.getNombre())
print(profesor1.getDepartamento())
print(profesor1.getCategoria())
print(profesor1.setCategoria("Ocacional"))
print(profesor1.getCategoria())