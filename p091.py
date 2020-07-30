# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:00:38 2020

@author: zhixia liu
"""
"""
Project Euler 91: Right triangles with integer coordinates

The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 ≤ x1, y1, x2, y2 ≤ 2.


Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
"""
#%% naive
from helper import reducefrac


def rectangle(uplimit):
    total = 0
    for vx in range(uplimit+1):
        for vy in range(uplimit+1):
            if vx==0 and vy==0:
                total += uplimit**2
                continue
            elif vx == 0 or vy == 0:
                total += uplimit
                continue
            dx,dy = reducefrac(vy,vx)
            total += min((uplimit-vy)//dy,vx//dx)+min((uplimit-vx)//dx,vy//dy)
    return total

print(rectangle(50))
        