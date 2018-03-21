#!/usr/bin/env python
#encoding : utf -8


import sys
slownik={}
zmienna = input("Ciag znakow do przeszukania : ")

with open(sys.argv[1],"r") as plik:
    for linia in plik:
        for slowo in linia.split():
            if(zmienna == zmienna):
                slownik[zmienna] += 1
            else:
                slownik[zmienna] = 1
                
print slownik.find(zmienna)


