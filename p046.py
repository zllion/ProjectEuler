# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 12:10:13 2020

@author: zhixia liu
"""

"""
Project Euler 46: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

#%% naive

from helper import prime_list
from math import sqrt
import sys
prime = prime_list()
def isdoublesquare(n):
    t = sqrt(n/2)
    return t.is_integer()

n = 7
while True:
    n += 2
    if prime.isPrime(n):
        continue
    prime.generateToN(n)
    for p in prime:
        if p>n:
            print(n)
            sys.exit(0)
        if isdoublesquare(n-p):
            break
    else:
        print(n)
        break