# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:09:25 2020

@author: zhixia liu
"""

"""
Project Euler 40: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

#%% naive, prime first

from helper import EratisthenesSieve
from time import time

s = time()
def isPandigital(n):
    n = ''.join(sorted(str(n)))
    for i in range(10):
        if n == '123456789'[:i+1]:
            return True
    return False

for n in EratisthenesSieve(7654321):
    if isPandigital(n):
        # print(n)
        continue
print(time()-s)

#%% naive, Pandigit first

from itertools import permutations
from helper import isPrime
s=time()
for n in permutations('1234567',7):
    n = int(''.join(n))
    if isPrime(n):
        # print(n)
        continue
print(time()-s)