import csv
import json

from csvajson.estudiante import Estudiante


class Archivo:
    def __init__(self, ruta: str) -> None:
        self.ruta = ruta

    def Archivocsv(self) -> list[Estudiante]:
        try:
            estudiantes = []
            with open(self.ruta) as file:
                leercsv = csv.reader(file)
                for fila in leercsv:
                    id, nombre, apellido = fila
                    estudiantes.append(Estudiante(id, nombre, apellido))
            return estudiantes
        except FileNotFoundError:
            raise FileNotFoundError(f"el archivo {self.ruta} no existe")

    def Escribirjson(self, estudiantes: list[Estudiante]):
        try:
            data = [Estudiante.diccionarioEstudiantes() for Estudiante in estudiantes]
            contenidojson = json.dumps(data, ensure_ascii=False)
            rutajson = self.ruta.replace(".csv", ".json")
            self.Guardarjson(rutajson, contenidojson)
        except Exception as error:
            print(error)
            raise error
        
    def Guardarjson(self, ruta, txt):
        with open(ruta, mode="w") as file:
                file.write(txt)