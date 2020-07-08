# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:11:14 2020

@author: zhixia liu
"""

"""
Project Euler 60: Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
#%% naive bf

from helper import prime_list
import sys
from time import time

st = time()

prime = prime_list(10000)
limit = prime.n

graph = {}

def dualconcatprime(m,n):
    return (prime.isPrime(int(str(m)+str(n))) and prime.isPrime(int(str(n)+str(m))))

def intersection(lst1,lst2):
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

for i,p1 in enumerate(prime):
    for p2 in prime[i+1:limit]:
        if dualconcatprime(p1,p2):
            graph.setdefault(p1,[]).append(p2)
            graph.setdefault(p2,[]).append(p1)

for k1,l2 in graph.items():
    for k2 in l2:
        if k2<k1: continue
        l3 = intersection(graph[k1],graph[k2])
        if l3:
            for k3 in l3:
                if k3<k2: continue
                l4 = intersection(graph[k3],l3)
                if l4:
                    for k4 in l4:
                        if k4<k3 : continue
                        l5 = intersection(graph[k4],l4)
                        if l5:
                            print(k1,k2,k3,k4,l5[0])
                            print(k1+k2+k3+k4+l5[0])
                            print(time()-st)
                            sys.exit(0)
print(time()-st)