
class Estudiante:
    def __init__(self, id: str, nombre: str, apellido: str) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

    def diccionarioEstudiantes(self) -> dict[str, str]:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
        }