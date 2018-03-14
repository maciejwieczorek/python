print('Podaj ilosc liczb :')
n = int(input())

i = 0
j = 0
tablica=[]

for i in range((n)):
    liczba = input()
    tablica.append(int(liczba))

print('Wpisz 1 posortuje rosnaco')
print('Wpisz 2 posortuje malejaco')
wybor = int(input())
print('wybierz zakres sortowania')

print('Zakres od : ')
zakres = int(input())

print('Zakres do :')
zakresDo = int(input())

zakresVol2 = zakres

if( wybor == 1):
    tablica.sort()
    for zakres in range(zakresDo):
        print(tablica[zakres])

elif(wybor == 2):
    tablica.sort()
    tablica.reverse()
    for zakresVol2 in range(zakresDo):
        print(tablica[zakresVol2])



