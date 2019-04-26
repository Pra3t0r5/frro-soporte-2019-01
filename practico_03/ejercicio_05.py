# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from frro_soporte_2019_01.practico_03.ejercicio_01 import crear_conexion
from frro_soporte_2019_01.practico_03.ejercicio_01 import reset_tabla
from frro_soporte_2019_01.practico_03.ejercicio_02 import agregar_persona
from frro_soporte_2019_01.practico_03.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    conn = crear_conexion()

    existe = buscar_persona(id_persona)

    if not existe:
        return False

    with conn:
        cur = conn.cursor()
        update = """
        update persona 
        set nombre = ?, dni = ?, fecha_nacimiento = ?, altura = ? 
        where id_persona = ?
        """
        nacimiento = datetime.datetime.strftime(nacimiento,"%Y-%m-%d")
        cur.execute(update, (nombre, dni, nacimiento, altura, id_persona))
        conn.commit()

    return True

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
