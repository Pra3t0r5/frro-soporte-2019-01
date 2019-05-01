# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from practico_03.ejercicio_01 import crear_conexion
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from practico_03.ejercicio_06 import reset_tabla


def agregar_peso(id_persona, fecha, peso):
    conn = crear_conexion()
    cur = conn.cursor()
    if buscar_persona(id_persona) and existe_reg_post(id_persona, fecha):
        consSQL = "INSERT INTO PersonaPeso(IdPersona, Fecha, Peso) VALUES (?,?,?)"
        tuplaDatos = (id_persona, datetime.datetime.strftime(fecha,"%Y-%m-%d"), peso)
        cur.execute(consSQL, tuplaDatos)
        cur.close()
        conn.commit()
        conn.close()
        return cur.lastrowid
    else:
        return False


def existe_reg_post(id_persona, fecha):
    conn = crear_conexion()
    cur = conn.cursor()
    consSQL = "SELECT fecha FROM PersonaPeso WHERE IdPersona = ? ORDER BY fecha DESC"
    tuplaDatos = (id_persona,)
    cur.execute(consSQL, tuplaDatos)
    rows = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    #PREGUNTAR ESTO TAMBIEN
    if rows:
        if rows[0][0] > fecha.strftime("%Y-%m-%d"):
            return False
        else:
            return True
    else:
        return True


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
