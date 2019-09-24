from frro_soporte_2019_01.practico_08.capa_datos.conexion import *
from frro_soporte_2019_01.practico_08.util.exceptions import NoExisteDni,DniRepetido

class DataUsuario(object):

    def buscar(self, id_usuario):
        """
        Devuelve la instancia del usuario, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Usuario
        """
        return self.session.query(Usuario).filter(Usuario.id_usuario == id_usuario).first()

    def buscar_dni(self, dni_usuario):
        """
        Devuelve la instancia del usuario, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Usuario
        """

        usu = self.session.query(Usuario).filter(Usuario.dni == dni_usuario).all()
        try:
            if not usu:
                raise NoExisteDni
        except:
            raise
        else:
            return self.session.query(Usuario).filter(Usuario.dni == dni_usuario).first()

    def get_all(self):
        """
        Devuelve listado de todos los usuarios en la base de datos.
        :rtype: list
        """
        return self.session.query(Usuario).all()

    def borrar_todos(self):

        """
        Borra todos los usuarios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        usuarios = self.todos()

        if not usuarios:
            return False
        for usu in usuarios:
            self.baja(usu.id_usuario)
        return True

    def alta(self, usuario):
        """
        Da de alta un nuevo usuario
        :type usuario: Usuario
        :rtype: Usuario
        """
        usu = self.session.query(Usuario).filter(Usuario.dni == usuario.dni).all()
        try:
            if usu:
                raise DniRepetido
            self.session.add(usuario)
        except:
            raise
        else:
            self.session.commit()


    def baja(self, dni_usuario):
        """
        Borra el usuario especificado por el dni.
        :rtype: bool
        """
        try:
            self.session.delete(self.buscar_dni(dni_usuario))
        except DniRepetido:
            raise
        except:
            raise
        else:
            self.session.commit()

    def modificacion(self, usuario):
        """
        Guarda un usuario con sus datos modificados.
        :type socio: Socio
        """
        soc = self.session.query(Usuario).filter(Usuario.dni == usuario.dni).all()
        try:
            if not soc:
                raise NoExisteDni
            self.session.query(Usuario).filter(Usuario.dni == usuario.dni).update({Usuario.nombre:usuario.nombre, Usuario.apellido:usuario.apellido, Usuario.direccion:usuario.direccion})
        except:
            raise
        else:
            self.session.commit()
