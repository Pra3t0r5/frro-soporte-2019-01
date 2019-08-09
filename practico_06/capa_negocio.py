# Implementar los metodos de la capa de negocio de socios.

from frro_soporte_2019_01.practico_05.ejercicio_01 import Socio
from frro_soporte_2019_01.practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    def __init__(self):
        super(DniRepetido, self).__init__('DNI repetido')


class LongitudInvalida(Exception):
    def __init__(self, campos_rangos):
        msg = ''
        for cr in campos_rangos:
            campo, min_max = cr
            min, max = min_max
            msg += 'Longitud de ' + campo + ' debe estar entre ' +\
                   str(min) + ' y ' + str(max) + '\n'
        super(LongitudInvalida, self).__init__(msg)


class MaximoAlcanzado(Exception):
    def __init__(self, maximo):
        super(MaximoAlcanzado, self).__init__('Se alcanzó el máximo de ' +
                                              str(maximo) + ' socios')


class NegocioSocio(object):
    MIN_CARACTERES_ABIERTO = 3
    MAX_CARACTERES_ABIERTO = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.todos()

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if self.regla_1(socio) and self.regla_2(socio) and self.regla_3():
                self.datos.alta(socio)
                return True
        except Exception as ex:
            raise ex

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
        Se deben validar las reglas 1 y 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            if self.regla_1(socio) and self.regla_2(socio):
                self.datos.modificacion(socio)
            return True
        except Exception as ex:
            raise ex

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        enc = self.buscar_dni(socio.dni)
        if enc is None or enc.id == socio.id:
            return True
        raise DniRepetido()

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        errores = []
        if not self.MIN_CARACTERES_ABIERTO < len(socio.nombre) < self.MAX_CARACTERES_ABIERTO:
            errores.append(('nombre', (self.MIN_CARACTERES_ABIERTO + 1, self.MAX_CARACTERES_ABIERTO - 1)))
        if not self.MIN_CARACTERES_ABIERTO < len(socio.apellido) < self.MAX_CARACTERES_ABIERTO:
            errores.append(('apellido', (self.MIN_CARACTERES_ABIERTO + 1, self.MAX_CARACTERES_ABIERTO - 1)))
        if len(errores) == 0:
            return True
        else:
            raise LongitudInvalida(errores)

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos()) < self.MAX_SOCIOS:
            return True
        raise MaximoAlcanzado(self.MAX_SOCIOS)

    def validar_todo(self, socio):
        """
        Validar las 3 reglas de negocio
        Si no validan, levanta la excepcion correspondiente.
        Devuelve True si las validaciones son exitosas.
        :type socio: Socio
        :rtype: bool
        """
        errores = []
        for r in zip((self.regla_1, self.regla_2, self.regla_3), (socio, socio, None)):
            try:
                regla, arg = r
                if arg is not None:
                    regla(arg)
                else:
                    regla()
            except Exception as ex:
                errores.append(ex)
        if len(errores) > 0:
            raise Exception(*errores)
        return True
