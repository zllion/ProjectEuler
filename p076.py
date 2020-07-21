# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:24:32 2020

@author: zhixia liu
"""

"""
Project Euler 76: Counting summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

#%% naive bf

from functools import lru_cache

@lru_cache(maxsize=None)
def countsum(n,leading):
    if n <=1 :
        return 1
    s = 0
    for i in range(1,min(n,leading)+1):
        s += countsum(n-i,i)
    return s


