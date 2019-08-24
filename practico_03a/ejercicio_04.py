# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from frro_soporte_2019_01.practico_03a.ejercicio_01 import reset_tabla
from frro_soporte_2019_01.practico_03a.ejercicio_02 import agregar_persona
from frro_soporte_2019_01.practico_03a.ejercicio_01 import session
from frro_soporte_2019_01.practico_03a.ejercicio_01 import Persona


def buscar_persona(id_persona):
    filas = session.query(Persona).filter(Persona.idPersona == id_persona).all()

    if not filas:
        return False

    persona = filas[0]
    fecha_nac = datetime.datetime.strptime(str(persona.fechaNacimiento), '%Y-%m-%d')
    return(persona.idPersona, persona.nombre, fecha_nac, persona.dni, persona.altura)




@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
