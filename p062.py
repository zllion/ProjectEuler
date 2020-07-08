# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:59:00 2020

@author: zhixia liu
"""

"""
Project Euler 62: Cubic permutations

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

#%% naive bf

d = {}
n=1
while True:
   key=''.join(sorted(str(n**3)))
   d.setdefault(key,[]).append(n)
   if len(d[key])==5:
       print(key)
       print(d[key])
       print(d[key][0]**3)
       break
   n += 1
   
