
import json # Importamos la librería json
class Ingestiones():
    def __init__(self):
        self.ruta_static = "C:/Users/USUARIO/Desktop/EVER/Repositorios/ever_macea2025/src/static/"
    def leer_json(self): # Funcion para leer un json
        ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        # r read: significa lectura, w write: significa escritura, a append: significa añadir
        with open(file=ruta_json, mode="r", encoding="utf-8") as f:
            datos = json.load(f)
        return datos
    
    def leer_txt(self): # Funcion para leer un txt
        ruta_txt = "{}txt/info.txt".format(self.ruta_static)
        # r read: significa lectura, w write: significa escritura, a append: significa añadir
        datos = ""
        with open(file=ruta_txt , mode="r", encoding="utf-8") as f:
            datos = f.read()
        return datos
    def leer_varios_txt(self, nombre=""): # Funcion para leer varios txt
        ruta_txt = "{}txt/{}".format(self.ruta_static, nombre)
        # r read: significa lectura, w write: significa escritura, a append: significa añadir
        datos = ""
        with open(file=ruta_txt , mode="r", encoding="utf-8") as f:
            datos = f.read()
        return datos
    def leer_cualquier_excel(self, nombre=""):
        ruta_excel = "{}excel/{}".format(self.ruta_static, nombre)
    def leer_cualquier_csv(self, nombre=""):
        ruta_csv = "{}csv/{}".format(self.ruta_static, nombre)
    def leer_html():
     pass
    def leer_bd():
        pass
    def leer_api():
        pass
    
    ############ CREAR FUNCION PARA ESCRIBIR EN UN ARCHIVO ############
    def escribir_txt(self, nombre, datos):
            ruta_txt = "{}.txt".format(nombre)
            with open(ruta_txt, mode="w", encoding="utf-8") as f:
                f.write(str(datos))
            
    
inges = Ingestiones()
datos_json = inges.leer_json()
print(datos_json)
print("<------------------------------------------------------------------------------------------------------------------>")
datos_txt = inges.leer_txt()
print(datos_txt)
print("<------------------------------------------------------------------------------------------------------------------>")
nombre_archivo = "info copy.txt"
datos_txt_dos = inges.leer_varios_txt(nombre_archivo)
print(datos_txt)


inges.escribir_txt(nombre="archivo_json", datos=datos_json)
inges.escribir_txt(nombre="archivo_txt", datos=datos_txt)
inges.escribir_txt(nombre="archivo_txt_dos", datos=datos_txt_dos)




# import os

# ruta_json = "C:/Users/USUARIO/Desktop/EVER/Repositorios/ever_macea2025/src/static"

# if os.path.exists(ruta_json):
#     print("✅ El archivo existe")
# else:
#     print("❌ El archivo NO existe")
