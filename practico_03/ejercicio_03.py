# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from frro_soporte_2019_01.practico_03.ejercicio_01 import reset_tabla
from frro_soporte_2019_01.practico_03.ejercicio_01 import crear_conexion
from frro_soporte_2019_01.practico_03.ejercicio_02 import agregar_persona




def borrar_persona(id_persona):
    conn = crear_conexion()

    with conn:
        cur = conn.cursor()
        consulta = "DELETE FROM persona WHERE id_persona = ?"
        cur.execute(consulta, (id_persona,))
        rta = cur.rowcount
        conn.commit()

    return rta == 1

@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
