# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:06:58 2020

@author: zhixia liu
"""

"""
Project Euler 35: Circular primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

from helper import EratisthenesSieve, isPrime
from tqdm import tqdm
result = []
primelist = EratisthenesSieve(1000000)
for i in tqdm(primelist):
    if all([isPrime(n) for n in [int(str(i)[-j:]+str(i)[:-j]) for j in range(1,len(str(i)))] ]):
        result.append(i)
print(result)
print(len(result))