# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_01 import crear_conexion


def agregar_persona(nombre, nacimiento, dni, altura):
    conn = crear_conexion()
    cur = conn.cursor()
    consSQL = "INSERT INTO persona(Nombre,FechaNacimiento,DNI,Altura) VALUES (?,?,?,?)"
    tuplaDatos = (nombre, datetime.datetime.strftime(nacimiento, '%Y-%m-%d'), dni, altura)
    cur.execute(consSQL,tuplaDatos)
    id = cur.lastrowid
    cur.close()
    conn.commit()
    conn.close()
    return id



@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
