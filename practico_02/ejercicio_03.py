# Implementar la clase Persona que cumpla las siguientes condiciones:
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


class Persona:
    sexosValidos = {"H","M"}
    
    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        if sexo in self.sexosValidos: 
            self.sexo 
        else:
            raise ValueError("results: debe ser uno de %r." % self.sexosValidos)
        self.peso = peso
        self.altura = altura

    def es_mayor_edad(self):
        pass

    # llamarlo desde __init__
    def generar_dni(self):
        pass

    def print_data(self):
        pass
