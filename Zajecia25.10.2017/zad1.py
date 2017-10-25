import math

class LiczbaZespolona:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.modul = self.__funModul()
    def __str__(self):
        return "%i + %ii" % (self.a, self.b)
    def __add__(self, other):
        return LiczbaZespolona(self.a + other.a, self.b + other.b)
    def __sub__(self, other):
        return LiczbaZespolona(self.a - other.a, self.b - other.b)
    def __mul__(self, other):
        return LiczbaZespolona(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
    def __div__(self, other):
        return LiczbaZespolona((self.a * other.a + self.b * other.b)/(math.pow(other.a,2) + math.pow(other.b,2)), (self.b * other.a - self.a * other.b)/(math.pow(other.a,2) + math.pow(other.b,2)))
    def __funModul(self):
        self.modul =  math.sqrt(math.pow(self.a, 2) + math.pow(self.b, 2))
    def __cmp__(self, other):
        return self.modul > other.modul


a = LiczbaZespolona(5, 1)
b = LiczbaZespolona(5, 1)
b = a
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
if(a == b):
    print("Sa rowne")
else:
    print("Nie sa rowne")