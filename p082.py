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

@lru_cache(maxsize=None)
def minimalpath(i,j,updown = 0):
    if j >= limit_j: 
        return 0
    if i== 0:
        if updown == 1:
            return m[i,j] + minimalpath(i,j+1)
        else:
            return m[i,j]+min(minimalpath(i+1,j,-1),minimalpath(i,j+1))
    elif i == limit_i-1:
        if updown == -1:
            return m[i,j] + minimalpath(i,j+1)
        else:
            return m[i,j]+min(minimalpath(i-1,j,1),minimalpath(i,j+1))
    else:
        if updown == 1:
            return m[i,j] + min(minimalpath(i-1,j,1),minimalpath(i,j+1))
        elif updown == -1:
            return m[i,j] + min(minimalpath(i+1,j,-1),minimalpath(i,j+1))
        else:
            return m[i,j] + min(minimalpath(i+1,j,-1),minimalpath(i-1,j,+1),minimalpath(i,j+1))

print(minimalpath(0,0))