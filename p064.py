# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 11:44:55 2020

@author: zhixia liu
"""

"""
Project Euler 64: Odd period square roots
All square roots are periodic when written as continued fractions and can be written in the form:

N−−√=a0+1a1+1a2+1a3+…
For example, let us consider 23−−√:23−−√=4+23−−√−4=4+1123√−4=4+11+23√−37
If we continue we would get the following expansion:

23−−√=4+11+13+11+18+…
The process can be summarised as follows:

a0=4,123√−4=23√+47=1+23√−37
a1=1,723√−3=7(23√+3)14=3+23√−32
a2=3,223√−3=2(23√+3)14=1+23√−47
a3=1,723√−4=7(23√+4)7=8+23−−√−4
a4=8,123√−4=23√+47=1+23√−37
a5=1,723√−3=7(23√+3)14=3+23√−32
a6=3,223√−3=2(23√+3)14=1+23√−47
a7=1,723√−4=7(23√+4)7=8+23−−√−4
It can be seen that the sequence is repeating. For conciseness, we use the notation 23−−√=[4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

2–√=[1;(2)], period=1
3–√=[1;(1,2)], period=2
5–√=[2;(4)], period=1
6–√=[2;(2,4)], period=2
7–√=[2;(1,1,1,4)], period=4
8–√=[2;(1,4)], period=2
10−−√=[3;(6)], period=1
11−−√=[3;(3,6)], period=2
12−−√=[3;(2,6)], period=2
13−−√=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N≤13, have an odd period.

How many continued fractions for N≤10000 have an odd period?
"""

#%% naive bf
from math import sqrt

odd = []
for n in range(2,10001):
    deci = []
    r = sqrt(n)
    while True and len(deci)<10000:
        integer = int(r)
        decimal = r - integer
        if decimal == 0:
            break
        label = str(decimal)[:8]
        if label in deci:
            i = deci.index(label)
            l = len(deci) - i # period
            if l%2 == 1:
                odd.append((n,l))
            print(n,l)
            break
        else:
            deci.append(label)
        r = 1/decimal
print(len(odd))

# round off error

#%%  sympy
from sympy import *

odd = []
for n in range(2,10001):
    deci = []
    r = sqrt(n)
    if isinstance(r,Integer):
        continue
    while True:
        integer = int(r.evalf())
        decimal = (r - integer).simplify()
        if decimal in deci:
            i = deci.index(decimal)
            l = len(deci) - i # period
            if l%2 == 1:
                odd.append((n,l))
            print(n,l)
            break
        else:
            deci.append(decimal)
        r = 1/decimal
print(len(odd))


#%% others

import math, itertools

def cf_period(r):
    p = int(math.sqrt(r))   # floor of sqrt(r)
    if p*p == r: return 0   # Square number
    q=1
    remainders = {}

    for pos in itertools.count(1):
        q=(r-(p*p))/q
        floor=int((math.sqrt(r)+p) /float(q))
        p = -1* (p- (floor*q))
        if (p,q) in remainders:
            return pos-remainders[p,q]
        remainders[p,q] = pos

print len([x for x in range(2,10001) if cf_period(x)%2==1])

#%% others 2


def odd_periodic_square(N):
    m = 0
    d = 1
    a = int(N**0.5)

    l = []

    while a != 2*int(N**0.5):
        m = d*a - m
        d = (N-m**2)//d
        if d == 0:
            return False
        else:
            a = (int(N**0.5) + m)//d
            l.append(a)
    
    return len(l)%2 != 0

count = 0
for n in range(2,10001):
    if odd_periodic_square(n):
        count += 1
print(count) 













