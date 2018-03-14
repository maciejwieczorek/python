def fLog1(x):
    return (x>0)

def fLog2(x):
    return not (x%2)

def fTest(flogiczna, liczba):
    if(flogiczna(liczba)):
        return ("OK")
    else:
        return ("NO")

print(fTest(fLog1, 5))
print(fTest(fLog2, 5))
