class DniRepetido(Exception):
    def __init__(self):
        super(DniRepetido, self).__init__('Ya existe un usuario con ese DNI')

class NoExisteDni(Exception):
    def __init__(self):
        super(NoExisteDni, self).__init__('No existe un usuario con ese Dni')
class NoExisteId(Exception):
    def __init__(self):
        super(NoExisteId, self).__init__('No existe un tipoUsuario con ese Id')
class IdRepetido(Exception):
    def __init__(self):
        super(IdRepetido, self).__init__('Ya existe un tipoUsuario con ese Id')
