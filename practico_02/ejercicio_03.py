<<<<<<< HEAD
# Implementar la clase Persona que cumpla las siguientes condiciones:
=======
# 3)Implementar la clase Persona que cumpla las siguientes condiciones:
>>>>>>> 1d53ddfd511b8e4f6f420c3c1a04c7e0b28a0fc1
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

<<<<<<< HEAD

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
=======
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
>>>>>>> 1d53ddfd511b8e4f6f420c3c1a04c7e0b28a0fc1
            return True
        else:
            return False

<<<<<<< HEAD
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
=======
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
>>>>>>> 1d53ddfd511b8e4f6f420c3c1a04c7e0b28a0fc1
