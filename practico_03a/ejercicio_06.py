# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from frro_soporte_2019_01.practico_03a.ejercicio_01 import crear_tabla, borrar_tabla
from frro_soporte_2019_01.practico_03a.ejercicio_01 import Base, Persona
from sqlalchemy import Column, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship
from frro_soporte_2019_01.practico_03a.ejercicio_01 import session, engine

class PersonaPeso(Base):

    __tablename__ = 'personaPeso'
    idPeso = Column(Integer, primary_key=True)
    peso = Column(Integer)
    fecha = Column(Date, nullable=False)
    id_persona = Column(Integer, ForeignKey('persona.idPersona'))
    persona = relationship(Persona)


def crear_tabla_peso():
    Base.metadata.create_all(engine)

def borrar_tabla_peso():
    PersonaPeso.__table__.drop(engine)

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
