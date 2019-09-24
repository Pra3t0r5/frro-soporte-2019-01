class DniRepetido(Exception):
    def __init__(self):
        super(DniRepetido, self).__init__('Ya existe un usuario con ese DNI')

class NoExisteDni(Exception):
    def __init__(self):
        super(NoExisteDni, self).__init__('No existe un usuario con ese Dni')
