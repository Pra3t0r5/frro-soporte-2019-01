# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento: datetime.datetime):
        self.fecha_nacimiento = nacimiento

    def edad(self):
        ahora = datetime.datetime.now()
        edad_aprox = ahora.year - self.fecha_nacimiento.year

        if self.fecha_nacimiento.month > ahora.month:
            return edad_aprox
        elif self.fecha_nacimiento.month == ahora.month:
            if self.fecha_nacimiento.day < ahora.day:
                return edad_aprox - 1
            return edad_aprox
        else:
            return edad_aprox - 1
