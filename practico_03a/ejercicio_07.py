# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from frro_soporte_2019_01.practico_03a.ejercicio_01 import session
from frro_soporte_2019_01.practico_03a.ejercicio_02 import agregar_persona
from frro_soporte_2019_01.practico_03a.ejercicio_04 import buscar_persona
from frro_soporte_2019_01.practico_03a.ejercicio_06 import PersonaPeso, reset_tabla


def agregar_peso(id_persona, fecha, peso):

    if buscar_persona(id_persona) and existe_registro_posterior(id_persona, fecha):
        perPeso = PersonaPeso()
        perPeso.id_persona = id_persona
        perPeso.peso = peso
        perPeso.fecha = fecha

        session.add(perPeso)
        session.commit()
        idPeso = (session.query(PersonaPeso).filter(PersonaPeso.id_persona ==id_persona).order_by(PersonaPeso.fecha.desc()).first()).idPeso
        return idPeso
    else:
        return False

def existe_registro_posterior(id_persona, fecha):
    rows = session.query(PersonaPeso).filter(PersonaPeso.id_persona == id_persona).order_by(PersonaPeso.fecha.desc()).all()
    if rows:
        for n in rows:
            if str(n.fecha) > fecha.strftime("%Y-%m-%d"):
                return False
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
