class punto:
    def __init__(self, x: int, y: int ):
        self.x: int = x
        self.y: int = y

    def mostrar (self):
        print (f"el punto x es: {self.x}, y el punto y es: {self.y} del plano cartesiano")

    def mover_punto (self, x, y):
        self.x = x
        self.y = y

    def calcular_distacia (self, z: int):
        distancia_x= z.x - self.x
        distancia_y= z.y - self.y
        distancia_z= (distancia_x**2 + distancia_y**2)**0.5
        return distancia_z

p1= punto(2, 6)
p2= punto (4, 8)
distancia= p1.calcular_distacia(p2)
print(f"la distacia es: {distancia}")
