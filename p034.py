# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:52:19 2020

@author: zhixia liu
"""

""" 
Project Euler 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

#%% naive

from math import factorial

f_list = [factorial(n) for n in range(10)]

result = []
for n in range(3,f_list[9]*7):
    if sum([f_list[int(i)] for i in str(n)]) == n:
        result.append(n)
print(result)
print(sum(result))