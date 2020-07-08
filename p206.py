# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:31:43 2020

@author: zhixia liu
"""

"""
Project Euler 206 Concealed Square

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

"""
from math import sqrt
from tqdm import tqdm
for i in tqdm(range(int(sqrt(1020304050607080900)),int(sqrt(1929394959697989900))+1,10)):
    square = str(i**2)
    for d in range(9):
        if square[d*2] != str(d+1):
            break
    else:
        print(i)
        break

    
    
    