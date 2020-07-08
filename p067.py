# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:57:36 2020

@author: zhixia liu
"""

""" 
Project Euler 67: Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

"""

#%% memoization
from functools import lru_cache
from timeit import timeit

with open('p067_triangle.txt','r') as f:
    triangle = [[int(i) for i in l.split(' ')] for l in f]

@lru_cache(maxsize = None)
def maxpath(i,j):
    if i+1 > len(triangle):
        return 0
    if j+1 > len(triangle[i]):
        return 0
    else:
        return triangle[i][j]+max(maxpath(i+1,j),maxpath(i+1,j+1))
print(maxpath(0,0))
print(timeit(lambda: maxpath(0,0),number=100))