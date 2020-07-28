# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 22:49:08 2020

@author: zhixia liu
"""
"""

Project Euler 82: Path sum: three ways

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

 
Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

#%% naive


import numpy as np
from functools import lru_cache
m=np.loadtxt(open('p082_matrix.txt', "rb"), delimiter=",", skiprows=0)

limit_i,limit_j = m.shape

cumulative = np.zeros(m.shape)
#initiallize
cumulative[:,limit_j-1]=m[:,limit_j-1]
for j in range(limit_j-2,-1,-1):
    for i in range(limit_i):
        minipath = cumulative[i,j+1]
        upper = 0
        iu=i-1
        while iu>=0 and upper<minipath:
            upper += m[iu,j]
            minipath = min(upper+cumulative[iu,j+1],minipath)
            iu -= 1
        below = 0
        ib = i+1
        while ib<limit_i and below<minipath:
            below += m[ib,j]
            minipath = min(below+cumulative[ib,j+1],minipath)
            ib += 1
        cumulative[i,j]=minipath+m[i,j]
print(min(cumulative[:,0]))