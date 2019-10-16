from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, String,
                        text, create_engine)
from sqlalchemy.orm import relationship

from . import db


class CabeceraDetalle(db.Model):
    __tablename__ = 'cabecera_detalle'

    idcabecera = db.Column(Integer, primary_key=True)
    importe_total = db.Column(Float(asdecimal=True),
                              server_default=text("'0'"))
    pedido = db.Column(ForeignKey('pedido.idpedido',
                                  onupdate='CASCADE'), nullable=False, index=True)

    pedido1 = db.relationship('Pedido')

    def ver(self):
        return '<DetailHead {}>'.format(self.idcabecera)


class HistorialStock(db.Model):
    __tablename__ = 'historial_stock'

    idhistorial_stock = db.Column(Integer, primary_key=True)
    fecha_hora_movimiento = db.Column(DateTime, nullable=False, server_default=text(
        "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    cantidad = db.Column(Float(asdecimal=True), nullable=False,
                         server_default=text("'0'"))
    unidad = db.Column(Integer, nullable=False)
    signo = db.Column(Integer, nullable=False, server_default=text("'0'"))
    linea_detalle = db.Column(Integer)

    def ver(self):
        return '<History {}>'.format(self.idhistorial_stock)


class Ingrediente(db.Model):
    __tablename__ = 'ingrediente'

    idingrediente = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(45), nullable=False)
    descripcion = db.Column(String(120))
    cantidad = db.Column(Float(asdecimal=True), nullable=False)
    unidad = db.Column(ForeignKey('unidad.idunidad',
                                  onupdate='CASCADE'), nullable=False, index=True)

    unidad1 = db.relationship('Unidad')

    def ver(self):
        return '<Ingredient {}>'.format(self.nombre)


class LineaDetalle(db.Model):
    __tablename__ = 'linea_detalle'

    idlinea_detalle = db.Column(Integer, primary_key=True)
    cabecera = db.Column(ForeignKey('cabecera_detalle.idcabecera',
                                    onupdate='CASCADE'), nullable=False, index=True)
    producto = db.Column(ForeignKey('producto.idproducto',
                                    onupdate='CASCADE'), nullable=False, index=True)
    cantidad = db.Column(Float(asdecimal=True))
    subtotal = db.Column(Float(asdecimal=True))

    cabecera_detalle = db.relationship('CabeceraDetalle')
    producto1 = db.relationship('Producto')

    def ver(self):
        return '<DetailLine {}>'.format(self.idlinea_detalle)


class Pedido(db.Model):
    __tablename__ = 'pedido'

    idpedido = db.Column(Integer, primary_key=True)
    nro_pedido = db.Column(Integer, nullable=False)
    estado = db.Column(String(45))
    fecha_hora_entrega = db.Column(DateTime)
    orden_fabricacion = db.Column(Integer)
    solicitante = db.Column(ForeignKey('usuario.id_usuario'),
                            nullable=False, index=True)

    usuario = db.relationship('Usuario')

    def ver(self):
        return '<Delivery {}>'.format(self.nro_pedido)


class Producto(db.Model):
    __tablename__ = 'producto'

    idproducto = db.Column(Integer, primary_key=True)
    nombre = db.Column(String(45), nullable=False)
    descripcion = db.Column(String(256))
    importe_unitario = db.Column(Float(asdecimal=True), nullable=False)
    unidad = db.Column(ForeignKey('unidad.idunidad',
                                  onupdate='CASCADE'), nullable=False, index=True)
    ingrediente = db.Column(ForeignKey(
        'ingrediente.idingrediente', onupdate='CASCADE'), nullable=False, index=True)

    ingrediente1 = db.relationship('Ingrediente')
    unidad1 = db.relationship('Unidad')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def ver(self):
        return '<Product {}>'.format(self.nombre)


class TipoUsuario(db.Model):
    __tablename__ = 'tipo_usuario'

    id_tipo_usuario = db.Column(Integer, primary_key=True)
    descripcion = db.Column(String(120))

    def ver(self):
        return '<User {}>'.format(self.id_tipo_usuario)


class Unidad(db.Model):
    __tablename__ = 'unidad'

    idunidad = db.Column(Integer, primary_key=True)
    abreviacion = db.Column(String(10), nullable=False)
    descripcion = db.Column(String(120))

    def ver(self):
        return '<User {}>'.format(self.abreviacion)


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(Integer, primary_key=True)
    username = db.Column(String(45), nullable=False, unique=True)
    password = db.Column(String(45), nullable=False)
    email = db.Column(String(120), nullable=False, unique=True)
    nombre = db.Column(String(120))
    apellido = db.Column(String(120))
    cuit = db.Column(Integer, unique=True)
    es_usuario = db.Column(Integer)
    dni = db.Column(Integer, unique=True)
    razon_social = db.Column(String(120))
    tipo_usuario = db.Column(ForeignKey(
        'tipo_usuario.id_tipo_usuario'), nullable=False, index=True)

    tipo_usuario1 = db.relationship('TipoUsuario')

    def __init__(self, idu, passw, username, email):
        self.id_usuario=idu
        self.password=passw
        self.username=username
        self.email=email
        self.nombre="nombre"
        self.apellido="apellido"
        self.es_usuario=True
        self.razon_social="albertecno"
        self.tipo_usuario=1

    def ver(self):
        return '<User {}>'.format(self.username)

def crear(objeto):
    try:
        db.session.add(objeto)
        db.session.commit()        
    except:
        db.session.rollback() 
        return False
    return True

def crearMuchos(*objetos):
    try:
        db.session.bulk_save_objects(objetos)
        db.session.commit()
    except:
        db.session.rollback() 
        return False
    return True

def borrarTodos(objeto):
    try:
        num_rows_deleted = db.session.query(objeto).delete()
        db.session.commit()
    except:
        db.session.rollback() 
        return 0
    return num_rows_deleted