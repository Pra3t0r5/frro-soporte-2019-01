# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from . import ejercicio_01 as ej01
#from practico_03.ejercicio_01 import reset_tabla


def agregar_persona(nombre, nacimiento, dni, altura):
    cSQL= "INSERT into Persona(Nombre,FechaNacimiento,DNI,Altura) VALUES(?,?,?,?)"
    tdatos = (nombre, nacimiento, dni, altura)
    ej01.cur.execute(cSQL,tdatos)
    return ej01.cur.lastrowid

@ej01.reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
