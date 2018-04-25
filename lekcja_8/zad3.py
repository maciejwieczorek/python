#! /usr/bin/env python

import subprocess
import os

import operator
import functools as fun

def primeFactorization(num): 
    num = num
    primes = []
    result = []
    if num > 1:
        [primes.append(x) for x in range(2, num) if all(x % y != 0 for y in range(2, x))]
    multy = fun.reduce(operator.mul, result, 1)
    for number in primes:
        if num % number == 0:
            result.append(number)

    multy = fun.reduce(operator.mul, result, 1)
    y = num/multy
    if y != 1 and y in primes:
        result.insert(0, int(y))
    return result
    
print(primeFactorization(756))
 

    
    
