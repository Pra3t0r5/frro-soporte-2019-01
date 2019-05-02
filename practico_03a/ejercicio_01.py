from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, Date, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from .config import SQLALCHEMY_DATABASE_URI

Base = declarative_base()

class Persona(Base):
    __tablename__='personas'
    idPersona = Column(Integer, primary_key=True)
    nombre = Column(String(30))
    fechaNacimiento = Column(Date)
    dni = Column(Integer)
    altura = Column(Integer)

engine = create_engine(SQLALCHEMY_DATABASE_URI)#, echo = True)
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def crear_tabla():
    Base.metadata.create_all(engine)

def borrar_tabla():
    Persona.__table__.drop(engine);

def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

