# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:02:59 2020

@author: zhixia liu
"""

"""
Project Euler 20: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

#%% naive
from math import factorial

print(sum([int(i) for i in str(factorial(100))]))