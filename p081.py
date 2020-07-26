# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 22:26:46 2020

@author: zhixia liu
"""
"""
Project Euler 81: Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

 
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.

"""

#%% naive


import numpy as np
from functools import lru_cache
m=np.loadtxt(open('p081_matrix.txt', "rb"), delimiter=",", skiprows=0)

limit_i,limit_j = m.shape

@lru_cache(maxsize=None)
def minimalpath(i,j):
    if i>= limit_i or j >= limit_j: 
        return 0
    if i == limit_i-1:
        return m[i,j]+minimalpath(i,j+1)    
    if j == limit_j-1:
        return m[i,j]+minimalpath(i+1,j)
    return m[i,j]+min(minimalpath(i+1,j),minimalpath(i,j+1))

print(minimalpath(0,0))