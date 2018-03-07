print('Podaj imie : ')
imie = input()

print('Pidaj nazwisko :')
nazwisko = input()

print('Podaj wiek :')
wiek = int(input())

if (wiek >= 18):
    print('Cześć ' + imie + ' ' + nazwisko + ', jesteś Pełnoletni')
else:
    print('Cześć ' + imie + ' ' + nazwisko + ', jesteś Niepełnoletni')


