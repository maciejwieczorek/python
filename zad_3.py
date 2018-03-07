import string
alfabetMaly = string.ascii_lowercase
alfabetDuzy = string.ascii_uppercase

size = alfabetMaly.__len__()

i = 0
while i < size:
    print(alfabetMaly[i] + alfabetDuzy[i])
    i += 1
