from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        text, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from . import db

Base = declarative_base()
metadata = Base.metadata


class CabeceraDetalle(Base):
    __tablename__ = 'cabecera_detalle'

    idcabecera = Column(Integer, primary_key=True)
    importe_total = Column(Float(asdecimal=True), server_default=text("'0'"))
    pedido = Column(ForeignKey('pedido.idpedido',
                               onupdate='CASCADE'), nullable=False, index=True)

    pedido1 = relationship('Pedido')


class HistorialStock(Base):
    __tablename__ = 'historial_stock'

    idhistorial_stock = Column(Integer, primary_key=True)
    fecha_hora_movimiento = Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    cantidad = Column(Float(asdecimal=True), nullable=False,
                      server_default=text("'0'"))
    unidad = Column(Integer, nullable=False)
    signo = Column(Integer, nullable=False, server_default=text("'0'"))
    linea_detalle = Column(Integer)


class Ingrediente(Base):
    __tablename__ = 'ingrediente'

    idingrediente = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(120))
    cantidad = Column(Float(asdecimal=True), nullable=False)
    unidad = Column(ForeignKey('unidad.idunidad',
                               onupdate='CASCADE'), nullable=False, index=True)

    unidad1 = relationship('Unidad')


class LineaDetalle(Base):
    __tablename__ = 'linea_detalle'

    idlinea_detalle = Column(Integer, primary_key=True)
    cabecera = Column(ForeignKey('cabecera_detalle.idcabecera',
                                 onupdate='CASCADE'), nullable=False, index=True)
    producto = Column(ForeignKey('producto.idproducto',
                                 onupdate='CASCADE'), nullable=False, index=True)
    cantidad = Column(Float(asdecimal=True))
    subtotal = Column(Float(asdecimal=True))

    cabecera_detalle = relationship('CabeceraDetalle')
    producto1 = relationship('Producto')


class Pedido(Base):
    __tablename__ = 'pedido'

    idpedido = Column(Integer, primary_key=True)
    nro_pedido = Column(Integer, nullable=False)
    estado = Column(String(45))
    fecha_hora_entrega = Column(DateTime)
    orden_fabricacion = Column(Integer)
    solicitante = Column(ForeignKey('usuario.id_usuario'),
                         nullable=False, index=True)

    usuario = relationship('Usuario')


class Producto(Base):
    __tablename__ = 'producto'

    idproducto = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(256))
    importe_unitario = Column(Float(asdecimal=True), nullable=False)
    unidad = Column(ForeignKey('unidad.idunidad',
                               onupdate='CASCADE'), nullable=False, index=True)
    ingrediente = Column(ForeignKey(
        'ingrediente.idingrediente', onupdate='CASCADE'), nullable=False, index=True)

    ingrediente1 = relationship('Ingrediente')
    unidad1 = relationship('Unidad')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TipoUsuario(Base):
    __tablename__ = 'tipo_usuario'

    id_tipo_usuario = Column(Integer, primary_key=True)
    descripcion = Column(String(120))


class Unidad(Base):
    __tablename__ = 'unidad'

    idunidad = Column(Integer, primary_key=True)
    abreviacion = Column(String(10), nullable=False)
    descripcion = Column(String(120))


class Usuario(Base):
    __tablename__ = 'usuario'

    id_usuario = Column(Integer, primary_key=True)
    username = Column(String(45), nullable=False, unique=True)
    password = Column(String(45), nullable=False)
    email = Column(String(120), nullable=False, unique=True)
    nombre = Column(String(120))
    apellido = Column(String(120))
    cuit = Column(Integer, unique=True)
    es_usuario = Column(Integer)
    dni = Column(Integer, unique=True)
    razon_social = Column(String(120))
    tipo_usuario = Column(ForeignKey(
        'tipo_usuario.id_tipo_usuario'), nullable=False, index=True)

    tipo_usuario1 = relationship('TipoUsuario')
