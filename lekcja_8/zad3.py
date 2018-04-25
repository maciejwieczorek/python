#! /usr/bin/env python

import subprocess
import os


from math import *
 
def rozklad(x):
    if x<=0:
        return 0
    i=2
    e=floor(sqrt(x))
    r=[] #używana jest tablica (lista), nie bepośrednie wypisywanie
    while i<=e:
        if x%i==0:
            r.append(i)
            x/=i
            e=floor(sqrt(x))
        else:
            i+=1
    if x>1: r.append(x)
        return r
 
 

rozklad(756)
print r
    
    
