
import json # Importamos la librería json
class Ingestiones():
    def __init__(self):
        self.ruta_static = "C:/Users/USUARIO/Desktop/EVER/Repositorios/ever_macea2025/src/static/"
    def leer_json(self):
        ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        # r read: significa lectura, w write: significa escritura, a append: significa añadir
        with open(file=ruta_json, mode="r", encoding="utf-8") as f:
            datos = json.load(f)
        return datos
    
inges = Ingestiones()
datos_json = inges.leer_json()
print(datos_json)

# import os

# ruta_json = "C:/Users/USUARIO/Desktop/EVER/Repositorios/ever_macea2025/src/static"

# if os.path.exists(ruta_json):
#     print("✅ El archivo existe")
# else:
#     print("❌ El archivo NO existe")
