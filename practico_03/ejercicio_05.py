# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from . import ejercicio_01 as ej01
from . import ejercicio_02 as ej02
from . import ejercicio_04 as ej04


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    conn = ej01.crear_conexion()
    cur = conn.cursor()
    update = "update persona set nombre = ?, fecha_nacimiento = ?, dni = ?, altura = ? where id_persona = ?"
    cur.execute(update, (nombre, nacimiento, dni, altura, id_persona))
    rta = cur.rowcount
    cur.close()
    conn.commit()
    conn.close()

    return False if rta == 0 else True


@ej01.reset_tabla
def pruebas():
    id_juan = ej02.agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert ej04.buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
