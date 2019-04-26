# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from frro_soporte_2019_01.practico_03.ejercicio_01 import crear_conexion
from frro_soporte_2019_01.practico_03.ejercicio_01 import reset_tabla
from frro_soporte_2019_01.practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    conn = crear_conexion()

    with conn:
        cur = conn.cursor()
        select = """
            SELECT id_persona, nombre, fecha_nacimiento, dni, altura 
            FROM persona 
            WHERE id_persona = ? 
            ORDER BY id_persona ASC
        """
        tdato = str(id_persona), # la coma es constructor de tuplas
        cur.execute(select, tdato)
        filas = cur.fetchall()

    if not filas:
        return False

    persona = filas[0]

    id_persona, nombre, fecha_nac, dni, altura = persona

    fecha_nac = datetime.datetime.strptime(fecha_nac, '%Y-%m-%d')

    return (id_persona, nombre, fecha_nac, dni, altura)

@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
