# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:06:43 2020

@author: zhixia liu
"""
"""
Project Euler 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

#%% naive
from sympy import isprime

n=600851475143

def LargestPrimeFactor(n):
    d=1
    q=n
    temp = d
    while d<=q:
        d += 1
        q,r=divmod(n,d)
        if r!=0:
            continue
        if isprime(q):
            return q
        if isprime(d):
            temp = d
    return temp

print(LargestPrimeFactor(n))