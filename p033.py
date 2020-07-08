# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:46:51 2020

@author: zhixia liu
"""

"""
Project Euler 33: Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

#%% naive


def cancelone(n1,n2):
    n1 = str(n1)
    n2 = str(n2)
    if n1[1]==n2[0] and n2[1]!='0':
        return (n1[0],n2[1])
    return None
pairs =[]
for i in range(11,99):
    for j in range(i+1,100):
        if cancelone(i,j) is not None:
            a,b=cancelone(i,j)
            if i/j == int(a)/int(b):
                pairs.append((a,b))
                print(i,j,a,b)
print(pairs)

#%% other's

import time
t=time.time()

for y in range(1,10):
    for z in range(y,10):
        x=float(9)*y*z/(10*y-z)
        if int(x) == x and y/z < 1 and x<10:
            print x, y, z, str(10*y+x)+'/'+str(z+10*x), str(y)+'/'+str(z)
print time.time()-t
