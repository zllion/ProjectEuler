# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:14:28 2020

@author: zhixia liu
"""

"""
Project Euler 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

#%% naive

def search():
    for a in range(500):
        for b in range(500):
            c = 1000-a-b
            if c<=0:
                break
            if a**2+b**2 == c**2:
                return a,b,c
    return None

print(search())