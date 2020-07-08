# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:40:38 2020

@author: zhixia liu
"""

"""
Project Euler 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

#%% naive

from tqdm import tqdm
d = {'n':0,'max_length':0,'chain':[]}

for n in tqdm(range(1,1000001)):
    chain = [n]
    while n > 1:
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n+1
        chain.append(n)
    if len(chain)>d['max_length']:
        d['max_length'] = len(chain)
        d['chain'] = chain
        d['n'] = chain[0]

print(d)