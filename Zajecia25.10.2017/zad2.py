import math

class Punkt2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def odleglosc(self, other):
        return math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2))

class Punkt3D(Punkt2D):
    def __init__(self, x, y, z):
        super(Punkt3D, self).__init__(x, y)
        self.z = z
    def odleglosc(self, other):
        return math.sqrt(math.pow(other.x - self.x, 2) + math.pow(other.y - self.y, 2) + math.pow(other.z - self.z, 2))

a = Punkt2D(1, 2)
c = Punkt2D(2, 2)
b = Punkt3D(1, 2, 3)
d = Punkt3D(2, 2, 2)
print(a.odleglosc(c))
print(b.odleglosc(d))