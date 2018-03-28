# !/usr/bin/env python
# encoding: utf -8
import sys

width = int(input("Wprowadz zakres : "))

def funkcja(plik, width):
    with open("test.txt") as plik:
        for index in range(0, len(plik), width):
        print(plik[index:index + width].center(width))
        plik.close()


with open("test.txt") as plik:
    funkcja(plik, width)
    print(plik)
    plik.close()

