# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:04:51 2020

@author: zhixia liu
"""

"""
Project Euler 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

#%% BF
from math import sqrt
amicable = []

def divisor(n):
    divisor = [1]
    for j in range(2,int(sqrt(n))+1):
        if n%j == 0:
            divisor.append(j)
            if n//j > j:
                divisor.append(n//j)
    return divisor
    
for i in range(1,10001):
    if i in amicable: 
        continue
    b = sum(divisor(i))
    if b == i:
        continue
    if sum(divisor(b))==i:
        amicable.append(i)
        if b<10000:
            amicable.append(b)
print(sum(amicable))