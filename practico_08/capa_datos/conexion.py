from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String,Date, Integer,Float, ForeignKey


class Conexion(object):

    def __init__(self):
        Base = declarative_base()
        class TipoUsuario(Base):
            __tablename__ = 'tipo_usuario'
            id_tipo_usuario = Column(Integer, primary_key=True, unique=True, autoincrement=True)
            descripcion = Column(String(50))
            usuario = relationship("Usuario")
        class Usuario(Base):
            __tablename__ = 'usuario'
            id_usuario = Column(Integer, primary_key=True, unique=True, autoincrement=True)
            nombre_usuario  = Column(String(50),unique=True)
            contraseña = Column(String(50))
            email = Column(String(30),unique=True)
            nombre = Column(String(250))
            apellido = Column(String(250))
            cuit = Column(Integer, unique=True,)
            dni = Column(Integer, unique=True,)
            razon_social = Column(String(50))
            direccion = Column(String(50))
            es_cliente = Column(Integer)
            id_tipo_usuario = Column(Integer, ForeignKey('tipo_usuario.id_tipo_usuario'))
            pedido = relationship("Pedido")
        class CabecerasDetalle(Base):
            __tablename__ = 'cabecera_detalle'
            id_pedido = Column(Integer,ForeignKey('pedido.id_pedido'),primary_key=True)
            id_cabecera_detalle = Column(Integer, primary_key=True, unique=True)
            importe_total=Column(Float)
            linea_detalle = relationship('LineaDetalle')
        class Pedido(Base):
            __tablename__ = 'pedido'
            id_pedido = Column(Integer, primary_key=True, unique=True, autoincrement=True)
            estado = Column(String(50))
            fechaEntrega = Column(Date)
            orden_fabricacion = Column(String(500))
            fecha_creacion = Column(Date)
            fecha_cancelacion = Column(Date)
            id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
            cabecera_detalle = relationship("CabecerasDetalle")
        class LineaDetalle(Base):
            __tablename__ = 'linea_detalle'
            id_linea_detalle = Column(Integer, primary_key=True, unique=True, autoincrement=True)
            cantidad_producto = Column(Integer)
            subtotal= Column(Float)
            id_cabecera_detalle = Column(Integer, ForeignKey('cabecera_detalle.id_cabecera_detalle'))
            id_pedido_cabecera = Column(Integer, ForeignKey('cabecera_detalle.id_pedido'))
            id_producto = Column(Integer, ForeignKey('producto.id_producto'))
            historial_stock = relationship('HistorialStock')
        class Producto(Base):
            __tablename__ = 'producto'
            id_producto = Column(Integer, primary_key=True, unique=True, autoincrement=True)
            nombre = Column(String(250))
            importe= Column(Float)
            descripcion = Column(String(250))
            linea_detalle = relationship('LineaDetalle')
        class Ingrediente(Base):
            __tablename__ = 'ingrediente'
            id_ingrediente = Column(Integer, primary_key=True, unique=True, autoincrement=True)
            nombre = Column(String(250))
        class ProductoIngrediente(Base):
            __tablename__ = 'producto_ingrediente'
            id_producto = Column(Integer, ForeignKey('producto.id_producto'),primary_key=True, unique=True)
            id_ingrediente = Column(Integer,ForeignKey('ingrediente.id_ingrediente'), primary_key=True, unique=True)
        class HistorialStock(Base):
            __tablename__ = 'historial_stock'
            id_historial_stock = Column(Integer, primary_key=True, unique=True, autoincrement=True)
            fecha = Column(Date)
            cantidad = Column(Integer)
            signo = Column(String(1))
            id_linea_detalle = Column(Integer, ForeignKey('linea_detalle.id_linea_detalle'))

        engine = create_engine('sqlite:///SistemaFinal.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine) #Crea las tablas

conec = Conexion();
