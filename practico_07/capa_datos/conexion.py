from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from frro_soporte_2019_01.practico_07.capa_datos.entidad import Base, Socio
from frro_soporte_2019_01.practico_07.util.exceptions import NoExisteDni,DniRepetido


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

        soc = self.session.query(Socio).filter(Socio.dni == dni_socio).all()
        try:
            if not soc:
                raise NoExisteDni
        except:
            raise
        else:
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
        Da de alta un nuevo socio
        :type socio: Socio
        :rtype: Socio
        """
        soc = self.session.query(Socio).filter(Socio.dni == socio.dni).all()
        try:
            if soc:
                raise DniRepetido
            self.session.add(socio)
        except:
            raise
        else:
            self.session.commit()


    def baja(self, dni_socio):
        """
        Borra el socio especificado por el dni.
        :rtype: bool
        """
        try:
            self.session.delete(self.buscar_dni(dni_socio))
        except DniRepetido:
            raise
        except:
            raise
        else:
            self.session.commit()

    def modificacion(self, socio):
        """
        Guarda un socio con sus datos modificados.
        :type socio: Socio
        """
        soc = self.session.query(Socio).filter(Socio.dni == socio.dni).all()
        try:
            if not soc:
                raise NoExisteDni
            self.session.query(Socio).filter(Socio.dni == socio.dni).update({Socio.nombre:socio.nombre, Socio.apellido:socio.apellido})
        except:
            raise
        else:
            self.session.commit()

