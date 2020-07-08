# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 09:33:30 2020

@author: zhixia liu
"""

"""
Project Euler 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

#%% naive

from sympy import primerange
from time import time
from math import sqrt

s=time()
print(sum(primerange(1,2000000)))
print(time()-s)

#%% improved
s=time()
def isprime(n,primelist):
    m = sqrt(n)
    for i in primelist:
        if i > m:
            return True
        if n%i == 0:
            return False
    return True

a=0
i=5
primelist =[2,3]
while i<2000000:
    if isprime(i,primelist):
        primelist.append(i)
    if isprime(i+2,primelist):
        primelist.append(i+2)
    i += 6
print(sum(primelist))

print(time()-s)

#%% Eratisthenes sieve
from helper import EratisthenesSieve

s = time()

limit = 2000000
primelist = EratisthenesSieve(limit)
a = 0
for i in primelist:
    a += i
print(a)
print(time()-s)