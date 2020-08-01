# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:43:29 2020

@author: zhixia liu
"""
"""
Project Euler 99: Largest exponential

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

#%% naive
from math import log

maxnumber = 0
maxline = 0
with open('p099_base_exp.txt','r') as f:
    l = 0
    for line in f:
        l += 1
        base,exponent = [int(i) for i in line.split(',')]
        n = exponent*log(base)
        if n > maxnumber:
            maxnumber = n
            maxline = l
print(maxline)