# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:56:08 2020

@author: zhixia liu
"""

"""
Project Euler 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

#%% naive
from math import factorial

digit=''
nlist=[0,1,2,3,4,5,6,7,8,9]
nth = 1000000-1 #numbers befor nth number
for i in range(9):
    l = len(nlist)-1
    q = nth//factorial(l)
    n = nlist[q] 
    digit += str(n)
    nth -= q*factorial(l)
    nlist.remove(n)
digit += str(nlist[0])
print(digit)
