# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

import datetime

from . import ejercicio_01 as ej01
from . import ejercicio_02 as ej02
from . import ejercicio_04 as ej04
from . import ejercicio_06 as ej06
from . import ejercicio_07 as ej07


def listar_pesos(id_persona):
    if ej04.buscar_persona(id_persona):
        conn = ej01.crear_conexion()
        cur = conn.cursor()
        select = "SELECT fecha, peso FROM Personapeso WHERE id_persona=? ORDER BY fecha ASC"
        cur.execute(select, (id_persona,))
        rows = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return False if not rows else rows
    else:
        return False

@ej06.reset_tabla
def pruebas():
    id_juan = ej02.agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    ej07.agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    ej07.agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
