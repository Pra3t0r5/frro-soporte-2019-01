# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    dni = Column(Integer)
    nombre = Column(String(250))
    apellido = Column(String(250))
