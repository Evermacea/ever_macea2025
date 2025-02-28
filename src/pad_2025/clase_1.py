# classs - relacion directa con un objecto (entidad u objeto)
# def - acciones o funciones del objeto

class Personas():
    def __init__(self):
        # atributos del objeto
        self.nombre = "Otoniel" # vatiable de tipo texto ""
        self.edad = 0 # variable de tipo numérico 0
        self.estatura = 100.0
        self.peso = 35.6 # variable de tipo decimal

persona = Personas() # Instanciar la clase o crear un objeto de la clase Personas


# Modificar los atributos del objeto persona

persona.nombre = "Otoniel Vazquez"
persona.edad = 25
persona.estatura = 1.80
persona.peso = 70

print("Nombre: ",persona.nombre) # Acceder al atributo nombre del objeto persona
print("Edad: ",persona.edad) # Acceder al atributo edad del objeto persona
print("Estarura :",persona.estatura) # Acceder al atributo estatura del objeto persona
print("Peso: ",persona.peso) # Acceder al atributo peso del objeto persona


import plotly.express as px
print("Plotly Express importado correctamente")