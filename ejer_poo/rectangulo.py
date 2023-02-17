
class rectangulo:
    def __init__(self, esqui1: int, esqui2: int):
        self.esqui1: int = esqui1
        self.esqui2: int = esqui2


    def calcu_area (self):
        altura = (self.esqui1 - self.esqui2)
        ancho = (self.esqui2 - self.esqui1)
        area = altura * ancho
        return area

    def calcu_perimetro (self):
        altura = (self.esqui1 - self.esqui2)
        ancho = (self.esqui2 - self.esqui2)
        perimetro=(altura*2) + (ancho*2)
        return perimetro

    def rec_cua (self):
        altura = (self.esqui1 - self.esqui2)
        ancho = (self.esqui2 - self.esqui1)
        if altura == ancho:
            return true
        else:
            return false

p1= esqui (9,6)
p2 = esqui (2,4)
rec= rectangulo (p1, p2)

print(f"el area del rectangulo es: {rec.calcu_area()}")
print (f"el perimetro del rectangulo es.{rec.calcu_perimetro()}")
print(f"el rectangulo es cuadrado {rec.rec_cua()}")



