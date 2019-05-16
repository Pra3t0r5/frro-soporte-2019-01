# Implementar los metodos de la capa de datos de socios.


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from frro_soporte_2019_01.practico_05.ejercicio_01 import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.session.query(Socio).filter(Socio.id == id_socio).first()

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.session.query(Socio).filter(Socio.dni == dni_socio).first()

    def todos(self):
        """
        Devuelve listado de todos los socios en la base de datos.
        :rtype: list
        """
        return self.session.query(Socio).all()

    def borrar_todos(self):

        """
        Borra todos los socios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socios = self.todos()

        if not socios:
            return False
        for soc in socios:
            self.baja(soc.id)
        return True

    def alta(self, socio: Socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.add(socio)
        self.session.commit()

        return socio

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        socio = self.buscar(id_socio)
        if socio == None:
            return False
        self.session.delete(socio)
        self.session.commit()
        return True

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        Devuelve el Socio modificado.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.query(Socio).filter(Socio.id == socio.id).update({Socio.dni:socio.dni, Socio.nombre:socio.nombre, Socio.apellido:socio.apellido})
        self.session.commit()

        return socio


def pruebas():
    # alta
    datos = DatosSocio()
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0

    # baja
    assert datos.baja(socio.id) == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0


if __name__ == '__main__':
    pruebas()
