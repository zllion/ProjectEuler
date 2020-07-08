# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:26:19 2020

@author: zhixia liu
"""

"""
Project Euler 36: Double-base palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

#%% naive


result = [i for i in range(1,1000001,2) if str(i)==str(i)[::-1] and bin(i)[2:]==bin(i)[:1:-1]]
print(result)
print(sum(result))