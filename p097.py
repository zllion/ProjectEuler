# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 12:35:21 2020

@author: zhixia liu
"""
"""
Project Euler 97: Large non-Mersenne prime

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.
"""
#%% naive

print(str(28433*2**7830457+1)[-10:])

#%% quick

width = 10000
n= int(str(2**width)[-10:])

tail = 1
power = 7830457
while power>width:
    tail = int(str(tail*n)[-10:])
    power -= width
tail = int(str(tail*2**power)[-10:])
tail = int(str(tail*28433+1)[-10:])