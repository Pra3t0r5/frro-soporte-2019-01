# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
from frro_soporte_2019_01.practico_03a.ejercicio_01 import reset_tabla
from frro_soporte_2019_01.practico_03a.ejercicio_01 import session
from frro_soporte_2019_01.practico_03a.ejercicio_01 import Persona
from frro_soporte_2019_01.practico_03a.ejercicio_02 import agregar_persona




def borrar_persona(id_persona):

    if session.query(Persona).filter(Persona.idPersona == id_persona).delete():
        session.commit()
        return True
    return False


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
