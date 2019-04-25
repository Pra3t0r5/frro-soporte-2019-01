# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from . import ejercicio_01 as ej01
from . import ejercicio_02 as ej02


def buscar_persona(id_persona):
    conn = ej01.crear_conexion()
    cur = conn.cursor()
    select = "SELECT id_persona, nombre, fecha_nacimiento, dni, altura FROM persona WHERE id_persona = ? ORDER BY id_persona ASC"
    cur.execute(select, id_persona)
    filas = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()

    return False if not filas else filas[0]

@ej01.reset_tabla
def pruebas():
    juan = buscar_persona(ej02.agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
