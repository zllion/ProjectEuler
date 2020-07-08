# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:25:51 2020

@author: zhixia liu
"""

"""
Project Euler 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

#%% fifth

fifth = []
for i in range(2,9**5*6):
    n = 0
    for j in str(i):
        n += int(j)**5
    if n == i:
        fifth.append(i)
print(fifth)
print(sum(fifth))