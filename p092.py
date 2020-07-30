# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:01:19 2020

@author: zhixia liu
"""
"""
Project Euler 92: Square digit chains
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
#%% naive


def squaredigit(n):
    return sum([int(i)**2 for i in str(n)])

total = 0
for i in range(1,10000001):
    while i != 1 and i != 89:
        i = squaredigit(i)
    else:
        if i == 89:
            total += 1

print(total)