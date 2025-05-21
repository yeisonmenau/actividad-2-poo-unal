class Persona():
    def __init__(self, nombre: str, apellido: str, numero_documento: str, año_nacimiento: int):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.año_nacimiento = año_nacimiento
    
    def mostrar_atributos(self) -> None:
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Numero de documento: {self.numero_documento}")
        print(f"Año de nacimiento: {self.año_nacimiento}\n")