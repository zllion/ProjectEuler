# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 13:52:00 2020

@author: zhixia liu
"""
"""
Project Euler 72: Counting fractions

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

"""

#%% naive bf

from helper import totient

total_frac = 0

for d in range(2,1000001):
    total_frac += totient(d)
    
print(total_frac)