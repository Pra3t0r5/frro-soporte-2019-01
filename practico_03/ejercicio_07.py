# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from . import ejercicio_01 as ej01
from . import ejercicio_02 as ej02
from . import ejercicio_04 as ej04
from . import ejercicio_06 as ej06


def agregar_peso(id_persona, fecha, peso):
    conn = ej01.crear_conexion()
    cur = conn.cursor()
    if ej04.buscar_persona(id_persona) and existe_registro_posterior(id_persona, fecha):
        insert = " INSERT INTO peso(idPersona, fecha, peso) VALUES(?,?,?)"
        tdatos = (id_persona, datetime.datetime.strftime(
        fecha, "%Y-%m-%d"), peso)
        cur.execute(insert, tdatos)
        cur.close()
        conn.commit()
        conn.close()
        return cur.lastrowid
    else:
        return False





def existe_registro_posterior(id_persona, fecha):
    conn = ej01.crear_conexion()
    cur = conn.cursor()
    select = "SELECT fecha FROM PersonaPeso WHERE id_persona=? ORDER BY fecha DESC"
    cur.execute(select, (id_persona,))
    rows = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    if rows:
        if rows[0][0] > fecha.strftime("%Y-%m-%d"):
            return False
        else:
            return True
    else:
        return True


@ej06.reset_tabla
def pruebas():
    id_juan = ej02.agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
