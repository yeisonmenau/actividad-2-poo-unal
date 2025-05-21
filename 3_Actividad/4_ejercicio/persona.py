class Persona:
    def __init__(self, nombre: str, direccion:str):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def setNombre(self, nombre: str):
        self.nombre = nombre
    def setDireccion(self, direccion: str):
        self.direccion = direccion