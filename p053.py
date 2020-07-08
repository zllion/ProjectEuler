# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:26:32 2020

@author: zhixia liu
"""

"""
Project Euler 53: Combinatoric selections

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (53)=10.

In general, (nr)=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: (2310)=1144066.

How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
"""

#%% naive bf

from scipy.special import comb

pairs = []
for n in range(23,101):
    for r in range(4,n-2):
        if comb(n,r)>1000000:
            pairs.append((n,r))
            
print(len(pairs))