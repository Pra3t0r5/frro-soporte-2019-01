# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_01 import crear_conexion


def buscar_persona(id_persona):
    conn = crear_conexion()
    cur = conn.cursor()
    consSQL = "SELECT * FROM persona WHERE IdPersona = ?"
    tuplaDatos = (id_persona,)
    #La coma es constructor de tuplas
    cur.execute = (consSQL,tuplaDatos)
    filas = cur.fetchall()
    #PREGUNTAR ESTO
    per = filas[0]
    id_per, nombre, fecha_nac, dni, altura = per
    fecha_nac = datetime.datetime.strptime(fecha_nac,'%Y-%m-%d')
    return (id_per, nombre, fecha_nac, dni, altura)
    
    if not filas:
        return False

#ANALIZAR ESTA OTRA FORMA
# with conn:
#        cur = conn.cursor()
#        select = """
#            SELECT id_persona, nombre, fecha_nacimiento, dni, altura 
#            FROM persona 
#            WHERE id_persona = ? 
#            ORDER BY id_persona ASC
#        """
#        tdato = str(id_persona), # la coma es constructor de tuplas
#        cur.execute(select, tdato)
#        filas = cur.fetchall()


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
