from frro_soporte_2019_01.practico_07.capa_datos.conexion import DatosSocio

class ControllerSocio(object):
    def __init__(self):
        self.datos = DatosSocio()

    def get_by_id(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar(id_socio)

    def get_by_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar_dni(dni_socio)

    def get_all(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.get_all()

    def alta(self, socio):
        """
        Da de alta un socio.
        :type socio: Socio
        :rtype: bool
        """
        self.datos.alta(socio)

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return self.datos.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        :type socio: Socio
        :rtype: bool
        """
        self.datos.modificacion(socio)
