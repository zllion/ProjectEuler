# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:37:54 2020

@author: zhixia liu
"""
"""
Project Euler 77: Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

#%% naive bf memoization

from functools import lru_cache
from helper import prime_list

prime = prime_list(5000)


@lru_cache(maxsize=None)
def countsum(n,leading):
    if n ==1 :
        return 0
    elif n==0:
        return 1
    s = 0
    i=0
    while True:
        p = prime[i]
        if p > leading or n-p<0:
            break
        s += countsum(n-p,p)
        i += 1
    return s

n=3
while True:
    s = countsum(n,n)
    if s>5000:
        print(n)
        break
    n+=1