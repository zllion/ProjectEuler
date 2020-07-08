# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 13:14:34 2020

@author: zhixia liu
"""

"""
Project Euler 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""


#%% naive
from time import time

s=time()
p = set()
for a in range(1, 100):
    for b in range(1, 9999 // a):
        if ''.join(sorted("%d%d%d" % (a, b, a*b))) == '123456789':
            p.add(a * b)
print(sum(p))
print(time()-s)
#%% improved busted

from itertools import permutations

s=time()
def remainnumbers(n1,n2):
    n1=str(n1)
    n2=str(n2)
    for c in n2:
        n1 = n1.replace(c,'')
    return n1

numberlist=set()
for n in permutations('123456789',4):
    n=''.join(n)
    if n.startswith('1') or n.startswith('2'):
        continue
    for d in permutations(remainnumbers('123456789',n),1):
        d=''.join(d)
        if int(n)%int(d) == 0:
            for q in permutations(remainnumbers('123456789',n+d),4):
                q=''.join(q)
                if str(int(n)//int(d)) == q:
                    numberlist.add(int(n))
                    break
    for d in permutations(remainnumbers('123456789',n),2):
        d=''.join(d)
        if int(n)%int(d) == 0:
            for q in permutations(remainnumbers('123456789',n+d),3):
                q=''.join(q)
                if str(int(n)//int(d)) == q:
                    numberlist.add(int(n))
                    break
print(numberlist)
print(sum(numberlist))
print(time()-s)