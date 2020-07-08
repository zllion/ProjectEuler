# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:55:38 2020

@author: zhixia liu
"""

"""
Project Euler 66: Diophantine equation

Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

#%% naive bf

from helper import isSquare, maxPrimeFactor
from tqdm import tqdm

def minimalsolution(d,limit=1000000000):
    p = maxPrimeFactor(d)
    x = p-1
    count = 1
    while True:
        if isSquare((x**2-1)/d):
            return x
        x += 2
        if isSquare((x**2-1)/d):
            return x
        if count>limit:
            print(None,d)
            return None
        x += p-2
        count += 1
D = [d for d in range(2,1001) if not isSquare(d)]
# X = [minimalsolution(d) for d in D]
X=[]
maxx = 2
for d in D:
    x = minimalsolution(d)
    if x is not None and x>maxx:
        maxx = x
        print(maxx)
    X.append(x)
print(maxx)

#%% naive bf 2
from math import sqrt
from helper import isSquare
def minimalsolution2(d,limit=1000000000):
    y = 1
    count = 1
    while True:
        x2 = y**2*d+1
        if isSquare(x2):
            return sqrt(x)
        if count>limit:
            print(None,d)
            return None
        y += 1
        count += 1
D = [d for d in range(2,1001) if not isSquare(d)]
# X = [minimalsolution(d) for d in D]
X=[]
maxx = 2
for d in D:
    x = minimalsolution(d)
    if x is not None and x>maxx:
        maxx = x
        print(maxx,d)
    X.append(x)
print(maxx)