# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from . import ejercicio_02 as ej02
from . import ejercicio_01 as ej01
#from practico_03.ejercicio_01 import reset_tabla
#from practico_03.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    cSQL= "DELETE FROM Persona WHERE IdPersona = ?"
    ej01.cur.execute(cSQL,id_persona)

    return False


@ej01.reset_tabla
def pruebas():
    assert borrar_persona(ej02.agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
