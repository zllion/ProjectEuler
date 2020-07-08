# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:05:06 2020

@author: zhixia liu
"""

"""
Project Euler 40: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""

#%% naive

s=''

for i in range(1,1000000):
    s += str(i)

p = 1
for j in [int(s[10**i-1]) for i in range(7)]:
    p *= j
    
print(p)

