# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 22:16:04 2020

@author: zhixia liu
"""

"""
Project Euler 80: Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

"""

#%% naive package
from helper import isSquare
from decimal import *
getcontext().prec=150
total = 0
for i in range(2,101):
    if isSquare(i):
        continue
    n = str(Decimal(i).sqrt())
    dot = n.find('.')
    total += sum([int(i) for i in n[:dot]+n[dot+1:101]])
print(total)

#%% cf long division

