<<<<<<< HEAD
# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.

import math


class Circulo:

    def __init__(self, radio):
        self.radio = radio
        self.calcular_area()

    def calcular_area(self):
        self.area = math.pi*self.radio**2

    def perimetro(self):
        return 2*math.pi*self.radio


circ = Circulo(10)
assert round(circ.area, 2) == 314.16
assert round(circ.perimetro(), 2) == 62.83
=======
import math

class Circulo:
    def __init__(self, radio):
        self.radio=radio

    def area(self):
        return math.pi*(self.radio**2)


    def perimetro(self):
        return 2*math.pi*self.radio
>>>>>>> 1d53ddfd511b8e4f6f420c3c1a04c7e0b28a0fc1
