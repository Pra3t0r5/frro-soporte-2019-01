from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Date, Integer


Base = declarative_base()
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name= Column(String(100))
    email = Column(String(100))
    username = Column(String(30))
    password = Column(String(100))
    register_date = Column(Date)

engine = create_engine('sqlite:///MyFlaskApp.db')
Base.metadata.bind = engine
db_session = sessionmaker()
db_session.bind = engine
session = db_session()
Base.metadata.create_all(engine) #Crea las tablas
