# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:57:28 2020

@author: zhixia liu
"""

"""
Project Euler 70: Totient permutation

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

#%% naive bf

from helper import totient
from tqdm import tqdm

results = []
for n in tqdm(range(2,10000000)):
    t = totient(n)
    if sorted(str(t)) == sorted(str(n)):
        results.append((n,t))

print(min(results[1:],key=lambda x: x[0]/x[1]))

#%% search primes around sqrt(10000000)