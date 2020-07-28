# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:59:01 2020

@author: zhixia liu
"""
"""
Project Euler 85: Counting rectangles

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""

#%% naive

# n(n+1)m(m+1)/4 = 2,000,000

from math import sqrt

# initialize
def squares(n,m):
    return n*(n+1)*m*(m+1)/4

def diff(n,m):
    return abs(squares(n,m)-2000000)
n = m = int(sqrt(sqrt(2000000)))

nearest = (n,m)
mindiff = diff(n,m)

while n>0:
    if squares(n,m)>2000000:
        n -= 1
    else:
        m += 1
    if diff(n,m)<mindiff:
        nearest = (n,m)
        mindiff = diff(n,m)
        print(nearest)
    