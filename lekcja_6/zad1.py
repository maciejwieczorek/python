import math

liczba = int(input("Podaj liczbe : "))

def funkcja(x):
   try:
        result = math.sqrt(x)
   except (TypeError, ValueError, ZeroDivisionError) as ex:
       print("Wyjatek nieoczekiwany blad")
       print(ex)
   else:
       print("Brak wyjatku")
       return result


print(funkcja(liczba))
