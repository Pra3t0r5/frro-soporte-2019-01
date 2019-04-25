import math

class Circulo:
    def __init__(self, radio):
        self.radio=radio

    def area(self):
        return math.pi*(self.radio**2)


    def perimetro(self):
        return 2*math.pi*self.radio
