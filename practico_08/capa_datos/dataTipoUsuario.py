from frro_soporte_2019_01.practico_08.capa_datos.conexion import *
from frro_soporte_2019_01.practico_08.util.exceptions import NoExisteId,IdRepetido

class DataTipoUsuario(object):

    def buscar_id(self, id_tipo_usuario):
        """
        Devuelve la instancia del tipoUsuario, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Usuario
        """
        tipo = self.session.query(TipoUsuario).filter(TipoUsuario.id_tipo_usuario == id_tipo_usuario).all()
        try:
            if not tipo:
                raise NoExisteId
        except:
            raise
        else:
            return self.session.query(TipoUsuario).filter(TipoUsuario.id_tipo_usuario == id_tipo_usuario).first()

    def get_all(self):
        """
        Devuelve listado de todos los tipos de usuarios en la base de datos.
        :rtype: list
        """
        return self.session.query(TipoUsuario).all()

    def borrar_todos(self):

        """
        Borra todos los Tipos de usuarios de la base de datos.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        tipos_usuarios = self.todos()

        if not tipos_usuarios:
            return False
        for tip in tipos_usuarios:
            self.baja(tip.id_tipo_usuario)
        return True

    def alta(self, tipo_usuario):
        """
        Da de alta un nuevo tipo usuario
        :type tipo_usuario: TipoUsuario
        :rtype: TipoUsuario
        """
        tipos = self.session.query(TipoUsuario).filter(TipoUsuario.id_tipo_usuario == tipo_usuario.id_tipo_usuario).all()
        try:
            if tipos:
                raise IdRepetido
            self.session.add(tipo_usuario)
        except:
            raise
        else:
            self.session.commit()


    def baja(self, id_tipo_usuario):
        """
        Borra el tipo_usuario especificado por el id.
        :rtype: bool
        """
        try:
            self.session.delete(self.buscar_id(id_tipo_usuario))
        except NoExisteId:
            raise
        except:
            raise
        else:
            self.session.commit()

    def modificacion(self, tipo_usuario):
        """
        Guarda un TipoUsuario con sus datos modificados de acuerdo a su id.
        :type tipo_usuario: TipoUsuario
        """
        tip = self.session.query(TipoUsuario).filter(TipoUsuario.id_tipo_usuario == tipo_usuario.id_tipo_usuario).all()
        try:
            if not tip:
                raise NoExisteId
            self.session.query(TipoUsuario).filter(TipoUsuario.id_tipo_usuario == tipo_usuario.id_tipo_usuario).update({TipoUsuario.descripcion:tipo_usuario.descripcion})
        except:
            raise
        else:
            self.session.commit()
