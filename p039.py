# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:27:29 2020

@author: zhixia liu
"""

"""
Project Euler 39: Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

#%% naive
from helper import divisor

def full_divisor(n):
    return sorted(divisor(n)+[n])
p_list = dict()

for n in range(1,333):
    divisorlist = full_divisor(n**2)
    for d in divisorlist[::-1]:
        if d+n>1000:
            continue
        elif (n**2/d+d)%2 == 1 or n**2/d>d:
            continue
        else:
            p_list.setdefault(n+d,set())
            p_list[n+d].add(tuple(sorted([n,(d+n**2/d)/2,(d-n**2/d)/2])))
            
print([(k,v) for k,v in sorted(p_list.items(), key=lambda l: len(l[1]))][-1])