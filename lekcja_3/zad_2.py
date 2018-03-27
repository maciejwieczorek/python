import math

class Punkt2D:

    x1 = None
    x2 = None
    y1 = None
    y2 = None

    punktA = [0, 0]
    punktB = [0, 0]

    def setX1(self, x1):
        self.x1 = x1

    def setX2(self, x2):
        self.x2 = x2

    def setY1(self, y1):
        self.y1 = y1

    def setY2(self, y2):
        self.y2 = y2

    def setPunktA(self):
        self.punktA = [self.setX1(), self.setY1()]

    def setPunktB(self):
        self.punktB = [self.setX2(), self.setY2()]

    def dlugosc(self):
        return math.sqrt(pow(self.setPunktB()[0] - self.setPunktA()[0], 2) + pow(self.punktB[1] - self.setPunktA()[1], 2))


p1 = Punkt2D()

p1.setX1(3)
p1.setX2(4)
p1.setY1(5)
p1.setY2(-2)

print(p1.dlugosc())