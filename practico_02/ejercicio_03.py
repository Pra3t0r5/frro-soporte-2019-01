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
    sexosValidos = {"H", "M"}

    def __init__(self, nombre, edad, sex, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = self.definir_sex(sex)
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()

    def definir_sex(self, sex):
        while(sex not in self.sexosValidos):
            if sex in self.sexosValidos:
                return sex
            else:
                raise ValueError("results: debe ser uno de %r." %
                                 self.sexosValidos)

    def es_mayor_edad(self):
        if(self.edad > 17):
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        return random.randint(1, 99999999)

    def print_data(self):
        print("Nombre: ", self.nombre, "\nDNI: ", self.dni, "\nEdad: ", self.edad,
              "\nSexo: ", self.sexo, "\nPeso: ", self.peso, "kg\nAltura: ", self.altura, "m")


per = Persona("Pepito Manolo", 25, "H", 87.6, 1.70)
per.print_data()
#assert(per.sexo) == "H"
assert(per.es_mayor_edad()) == True
