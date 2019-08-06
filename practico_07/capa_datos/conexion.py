from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from frro_soporte_2019_01.practico_07.capa_datos.entidad import Base, Socio


class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        db_session = sessionmaker()
        db_session.bind = engine
        self.session = db_session()
        Base.metadata.create_all(engine) #Crea la tabla socios

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

    def get_all(self):
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

    def alta(self, socio):
        """
        Devuelve el Socio luego de darlo de alta.
        :type socio: Socio
        :rtype: Socio
        """
        self.session.add(socio)
        self.session.commit()


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

