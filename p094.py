# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:32:31 2020

@author: zhixia liu
"""
"""
Project Euler 94: Almost equilateral triangles

It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""

#%% naive

from helper import isSquare
from tqdm import tqdm
limit = 1000000000
klimit = (limit+1)//3//2

# according to Helen formular, to be integer area, a=b=2k+1 ,c=a+1 or a-1
# only need to test (3k+1)(k+1) and (3k+2)k

totalperi = 0
for k in tqdm(range(1,klimit+1)):
    if isSquare((3*k+1)*(k+1)):
        peri = 6*k+2
        if peri<=limit:
            totalperi += peri
        else:
            print('exceed')
    if isSquare((3*k+2)*k):
        peri = 6*k+4
        if peri<=limit:
            totalperi += peri
        else:
            print('exceed')
            
print(totalperi) 
    