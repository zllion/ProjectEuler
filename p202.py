# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:01:00 2020

@author: zhixia liu
"""

"""
Project Euler 202 Laserbeam
Three mirrors are arranged in the shape of an equilateral triangle, with their reflective surfaces pointing inwards. There is an infinitesimal gap at each vertex of the triangle through which a laser beam may pass.

Label the vertices A, B and C. There are 2 ways in which a laser beam may enter vertex C, bounce off 11 surfaces, then exit through the same vertex: one way is shown below; the other is the reverse of that.


There are 80840 ways in which a laser beam may enter vertex C, bounce off 1000001 surfaces, then exit through the same vertex.

In how many ways can a laser beam enter at vertex C, bounce off 12017639147 surfaces, then exit through the same vertex?

"""
"""
2x+2y-3 = 12017639147
(y-x) mod 3 = 0
x,y coprime
"""
from tqdm import tqdm
def gcd(p,q):
    while q!=0:
        p,q = q,p%q
    return p
def is_coprime(x,y):
    return gcd(x,y) == 1
count = 0
for y in tqdm(range(2,6008819575,3)):
    if is_coprime(y,6008819575-y):
        count += 1
print(count)