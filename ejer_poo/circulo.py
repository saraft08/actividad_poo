import math

class circulo:
    def __init__(self, radio: float, centro: float):
        self.radio: float = radio
        self.centro: float= centro

    def calcu_area (self):
        area = math.pi * (self.radio**2)
        return area

    def calcu_perimetro (self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
    def p_circu (self, punto: float):
        distacia= self.centro.calcu_distacia(punto)
        if distacia <= self.radio:
            return true
        else:
             return false

r1= punto (8,6)
ra = circulo(r1, 4)
print(f"el area del circulo es: {ra.calcu_area()}")
print(f"el perimetro del rectangulo es.{ra.calcu_perimetro()}")
print(f"la distacia del punto es: {ra.p_circu(2,3)}")



