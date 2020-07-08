# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:43:58 2020

@author: zhixia liu
"""

"""
Project Euler 48: Self powers

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

"""

#%% bf
from time import time
t=time()
s = 0 
for i in range(1,1001):
    s += i**i
print(str(s)[-10:])
print(time()-t)

#%% bf2

t=time()
s = 0
for i in range(1,1001):
    s = int(str(s)[-10:]) + int(str(i**i)[-10:])
print(str(s)[-10:])
print(time()-t)    

    