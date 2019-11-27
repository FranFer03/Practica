class Caja:
    def __init__(self, largo, ancho, costo=10):
        self.largo = largo
        self.ancho = ancho
        self.costo = costo
    def perimentro(self):
        return 2*(self.largo + self.ancho)
    def area(self):
        return self.ancho * self.largo
    def precio(self):
        area = self.area()
        return area*self.costo

caja1 = Caja(2,2)
print(caja1.precio())