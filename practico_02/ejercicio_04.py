# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

from . import ejercicio_03 as ej03
import datetime


class Estudiante(ej03.Persona):
    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas): #añadir parametros persona
        super().__init__(nombre, edad, sexo, peso, altura)
        self.NomCarrera = carrera
        self.anioIngreso  = anio
        self.cantMaterias = cantidad_materias
        self.cantMatAprobadas = cantidad_aprobadas

    def avance(self):
        return print(str((self.cantMatAprobadas*100)/ self.cantMaterias) + "%")

    # implementar usando modulo datetime
    def edad_ingreso(self):
        return print(self.edad - (datetime.date.today().year - self.anioIngreso), "años")


es = Estudiante(nombre="Matías", edad=22, sexo='M', peso=87, altura=1.87,
                carrera="Sistemas", anio=2015, cantidad_materias=44, cantidad_aprobadas=35)
es.edad_ingreso()
es.print_data()
es.avance()

