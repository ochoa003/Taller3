from csvajson.archivo import Archivo
from csvajson.estudiante import Estudiante

try:
    #ruta del archivo
    archivo = Archivo("xyz")
    estudiantes = archivo.Archivocsv()
    archivo.Escribirjson(estudiantes)
    #leer json
    with open('estudiantes.json', mode="r", encoding="utf-8") as file:
        archivos = file.read()
        print(archivos)
    print(f"Estudiantes obtenidos: {len(estudiantes)}")
except Exception as error:
    print(error)