# 3)Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.
import random

class Persona:
    
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = int(edad)
        self.sexo = sexo
        self.peso = float(peso)
        self.altura = float(altura)
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

   # llamarlo desde __init__
    def generar_dni(self):
        dni=random.randrange(100000000)
        return dni

    def print_data(self):
        print("Datos personales: ")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Sexo: ", self.sexo)
        print("Peso: ", self.peso)
        print("Altura: ", self.altura)
        print("Dni: ", self.dni)
