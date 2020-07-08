# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:59:00 2020

@author: zhixia liu
"""

"""
Project Euler 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""

#%%
from math import sqrt
from helper import divisor



abundant = []

for i in range(1,28112):
    if sum(divisor(i))>i:
        abundant.append(i)

sieve = [False]*28123

for i in range(len(abundant)):
    for j in range(i,len(abundant)):
        if abundant[i]+abundant[j]<=28123:
            sieve[abundant[i]+abundant[j]-1]=True
s=0
for i in range(28123):
    if not sieve[i]:
        print(i+1)
        s += i+1
print(s)