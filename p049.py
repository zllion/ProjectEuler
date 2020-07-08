# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:56:03 2020

@author: zhixia liu
"""

"""
Project Euler 49: Prime permutations
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

#%% naive bf

from helper import prime_list
from itertools import permutations
import sys
prime = prime_list(10000)

def arithmseq(lst):
    temp = sorted(lst)
    for i in range(len(temp)-1):
        for j in range(i+1,len(temp)):
            dif = temp[j]-temp[i]
            if (temp[j]+dif) in temp:
                return [temp[i],temp[j],temp[j]+dif]
    return None
            
result=[]
skiplst = []
for i in prime:
    if i<1000:
        continue
    if i in skiplst: continue
    plst=[]
    for j in permutations(str(i),4):
        if j[0] == '0': continue
        j = int(''.join(j))
        if j in plst: continue
        if prime.isPrime(j):
            plst.append(j)
    skiplst += plst
    if len(plst)>=3:
        temp = arithmseq(plst)
        if temp is not None:
            result.append(temp)
print(result)

#%% others

def main():
    from helper import prime_list

    def sorted(seq):
        seq = list(seq)
        seq.sort()
        return "".join(seq)

    p = prime_list(10000)
    
    pd = {}
    for pi in p:
        if pi < 1000: continue
        spi = sorted(str(pi))
        pd.setdefault(spi, []).append(pi)
    
    for i, pi in enumerate(p):
        if pi < 1000 or pi == 1487: continue
        spi = sorted(str(pi))
        pals = pd[spi] 
        if len(pals) < 3: continue
        for pj in pals:
            if pj <= pi: continue 
            if sorted(str(pj)) != spi: continue
            diff = pj - pi
            pk = pj+diff
            if pk in pals:
                print("%s%s%s" % (pi, pj, pk))
                return
main()
