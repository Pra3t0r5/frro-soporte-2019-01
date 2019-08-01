from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    dni = Column(String(8))
    nombre = Column(String(250))
    apellido = Column(String(250))
