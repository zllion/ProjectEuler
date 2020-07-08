# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 14:23:51 2020

@author: zhixia liu
"""

"""
Project Euler 58: Spiral primes

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

#%% naive bf

from helper import prime_list

prime = prime_list(100000)
total = 2
p = 1
n = 3
side =2
position = 1
count_1 = 1
while p/total > 0.1:
    position += 1
    if position > 4:
        position =1
        side += 2
    n += side
    total += 1
    if prime.isPrime(n):
        p += 1
    count_1 += 1
    if count_1 %1000 == 0:
        print(p/total)
    # print(n)
    # if n>50:
    #     break
print(side+1)
    