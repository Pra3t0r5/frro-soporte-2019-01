#  Ejemplo basico ALCHEMY--------------------------------------
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker

#metadatos
Base = declarative_base()

#mapeos de tablas a clases
class User(Base):
    __tablename__ = 'users'  # indispensable
    id = Column(Integer, primary_key=True)  # indispensable
    name = Column(String)
    fullname = Column((String), nullable=False)
    password = Column(String(8))

class City(Base):
    __tablename__ = 'city'  # indispensable
    id = Column(Integer, primary_key=True)  # indispensable
    name = Column(String)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship("User")

#datos sqlite en la carpeta actual
# engine = create_engine('mysql://scott:tiger@localhost/foo')
engine = create_engine('sqlite:///sqlalchemy_ejemplo0.db')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()


def creaTabla():
    #crea todas las tablas definidas en los metadatos
    Base.metadata.create_all(engine)


def insertaReg():
    oper = User()
    oper.name = 'Juan'
    session.add(oper)

    oper = User()
    oper.name = 'Ailen'
    session.add(oper)

    session.commit()  # graba nuevos insert


def consulta():
    lu = session.query(User).all()  # lista
    print('Lista de usuarios:')
    for u in lu:
        print('Usuario: ', u.id, u.name)


if __name__ == '__main__':
    creaTabla()
    insertaReg()
    consulta()
