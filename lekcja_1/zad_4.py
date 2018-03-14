import string

alfabet = string.ascii_uppercase


print('Wprowadz n :')
n = int(input())

k = 0


for l in range(len(alfabet)):
    for j in range(n):
         print(alfabet[l])
