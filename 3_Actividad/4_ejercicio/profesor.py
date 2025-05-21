from persona import Persona
class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self._departamento = departamento
        self._categoria = categoria

    def getDepartamento(self) -> str:
        return self._departamento

    def getCategoria(self) -> str:
        return self._categoria

    def setDepartamento(self, departamento: str):
        self._departamento = departamento

    def setCategoria(self, categoria: str):
        self._categoria = categoria