# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 13:55:21 2020

@author: zhixia liu
"""

"""
Project Euler 47: Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

#%% naive

from helper import prime_list
from math import sqrt
prime = prime_list()

def primefactor(n):
    prime.generateToN(n/2)
    results = []
    for p in prime:
        if p>n/2:
            return results
        if n%p == 0:
            results.append(p)
    return results

factors = [1,1,1] # start from 2,3,4

n = 4
while True:
    n += 1
    l = len(primefactor(n))
    if l==4 and all([i==l for i in factors]):
        print(n-3)
        break
    else:
        factors = factors[1:]+[l]

#%% sieve method
Limit=1000000     # Search under 1 million for now
factors=[0]*Limit # number of prime factors.
count=0
for i in range(2,Limit):
    if factors[i]==0:
        # i is prime
        count =0
        val =i
        while val < Limit:
            factors[val] += 1
            val+=i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print(i-3) # First number
            break
    else:
        count = 0