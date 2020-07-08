# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:51:25 2020

@author: zhixia liu
"""

"""
Project Euler 31: Coin sums

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""

#%% 

from functools import lru_cache
from timeit import timeit
coinlist = [1,2,5,10,20,50,100,200]
@lru_cache(maxsize=None)
def coinsums(n,maxcoin):
    if n == 0:
        return 1
    sums = 0
    for i in coinlist:
        if n<i or i>maxcoin:
            break
        else:
            sums += coinsums(n-i,i)
            print(n,i,maxcoin,sums)
    return sums

print(coinsums(200,200))