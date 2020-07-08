# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:06:57 2020

@author: zhixia liu
"""

"""
Project Euler 56: Powerful digit sum

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

"""

#%% niave bf

def digitsum(n):
    n = str(n)
    return sum([int(i) for i in n])

maxsum = 0
for i in range(100):
    for j in range(100):
        s = digitsum(i**j)
        maxsum = max(maxsum,s)
print(maxsum)