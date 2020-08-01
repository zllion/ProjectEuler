# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:01:50 2020

@author: zhixia liu
"""
"""
Project Euler 95: Amicable chains

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
"""

#%% naive

from helper import divisor

def amicableChain(n,uplimit):
    temp = n
    chain = [n]
    while True:
        temp = sum(divisor(temp))
        # print(temp)
        if temp == n:
            break
        if temp in chain:
            # print('exit')
            return None
        if temp > uplimit:
            return None
        chain.append(temp)
    return chain

minchain = 0
minmember = 0
for i in range(1,1000000):
    temp = amicableChain(i,1000000)
    if temp is not None:
        if len(temp)>minchain:
            minmember = i
            minchain = len(temp)
print(minmember)

#%% euler post: tzaman's method: sieve + chain finder

lim = 1000000
div = [0]*lim #sieving for divisor sums
for i in range(1,lim):
    for j in range(2*i, lim, i):
        div[j] += i

chain = [0]*lim #chains: -1 = bad, 0 = untested, n = length of chain
chain[0] = -1
for i in range(1,lim):
    if chain[i]: continue
    seq = [i]
    while(div[seq[-1]]<lim and chain[div[seq[-1]]]==0 and div[seq[-1]] not in seq):
        seq.append(div[seq[-1]])
    if div[seq[-1]] in seq: #hit a loop
        loop = seq.index(div[seq[-1]])
        for l in range(0, loop):
            chain[seq[l]] = -1 #pre-loop: mark as bad
        for l in range(loop, len(seq)):
            chain[seq[l]] = len(seq)-loop #within-loop: mark chain length
    else: #exceeded lim or hit a bad number
        for s in seq: chain[s] = -1 #mark as bad
print(chain.index(max(chain)))