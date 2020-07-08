# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:22:37 2020

@author: zhixia liu
"""

"""
Project Euler 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

#%% naive
from sympy import prime

print(prime(10001))

