# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:58:44 2020

@author: zhixia liu
"""

"""
Project Euler 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

#%% naive
s=0
for i in range(3,1000,3):
    s += i
for i in range(5,1000,5):
    s += i
for i in range(15,1000,15):
    s -= i
print(s)