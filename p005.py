# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:56:13 2020

@author: zhixia liu
"""

"""
Project Euler 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

#%% naive
from functools import reduce
from helper import gcd

def smallestmultiple(a,b):
    factors = []
    for i in range(b,a-1,-1):
        if factors == []:
            factors.append(i)
            continue
        for j in factors:
            if i == 1:
                break
            i = i/gcd(i,j)
        else:
            factors.append(i)
    return reduce(lambda a,b: a*b, factors)

print(smallestmultiple(1,20))