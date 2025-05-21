from persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self._carrera = carrera
        self._semestre = semestre

    def getCarrera(self) -> str:
        return self._carrera

    def getSemestre(self) -> int:
        return self._semestre

    def setCarrera(self, carrera: str):
        self._carrera = carrera

    def setSemestre(self, semestre: int):
        self._semestre = semestre