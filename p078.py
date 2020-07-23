# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:53:14 2020

@author: zhixia liu
"""
"""
Project Euler 78: Coin partitions

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.

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

n=3
while True:
    s = countsum(n,n)
    if s%1000000==0:
        print(n)
        break
    n+=1