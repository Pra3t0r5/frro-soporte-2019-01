# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from . import ejercicio_04 as ej04


from collections import defaultdict
from typing import List


def organizar_estudiantes(estudiantes: List[ej04.Estudiante]):
    d = defaultdict(int)

    for es in estudiantes:
        d[es.carrera] += 1
    return d



