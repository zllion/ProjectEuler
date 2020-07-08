# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:21:34 2020

@author: zhixia liu
"""

"""
Project Euler 63: Powerful digit counts

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

#%% naive bf
from math import floor, ceil
d = {}
n = 1
while True:
    start = int('1'+'0'*(n-1))**(1/n)
    end = int('9'*n)**(1/n)
    if end-start > 1:
        temp = list(range(ceil(start),floor(end)+1))
        if len(str(temp[0]**n))!=n:
            del temp[0]
        try:
            if len(str(temp[1]**n))!=n:
                del temp[1]
        except: 
            pass
        d[n]=temp
        n+=1
    else:
        break


print(n-1)
print(d)
total = [v for k in d for v in d[k]]
print(len(total))

    