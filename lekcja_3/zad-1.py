import math

class LiczbaZespolona(object):

    zmienne =[0,0]

    def setZmienne(self, name, values):
        if(name == "im"):
            self.zmienne[1] = values
        elif (name == "re"):
            self.zmienne[0] = values
        elif(name == "zmienne"):
            self.zmienne[0] = values[0]
            self.zmienne[1] = values[1]

    def dodawanie(self):
        return self.zmienne[0] + self.zmienne[1]

    def odejmowanie(self):
        return self.zmienne[0] - self.zmienne[1]

    def mnozenia(self):
        return self.zmienne[0] * self.zmienne[1]

    def dzielenie(self):
        return self.zmienne[0] / self.zmienne[1]


    def modul(self):
        return math.fabs(math.sqrt(math.pow(self.zmienne[0], 2) + math.pow(self.zmienne[1], 2)))

obiekt = LiczbaZespolona()

obiekt.zmienne = (4, 5)

print(obiekt.dodawanie())
print(obiekt.odejmowanie())
print(obiekt.modul())