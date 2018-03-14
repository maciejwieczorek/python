import math

krotki = [ (1,2), (3,4), (5,6)]

for krotka in krotki:
    print("el 1 %d" % krotka[0])
    print("el 2 %d" % krotka[1])


def listaPunktow(lista, punkt):
    lista = [(krotki, len(krotki)) for krotki in lista.split()]

krotkiSort = sorted(krotki, key = lambda tup: tup[0])
print(krotkiSort)
