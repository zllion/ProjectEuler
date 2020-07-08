# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 14:19:21 2020

@author: zhixia liu
"""

"""
Project Euler 37: Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

#%% naive

from helper import isPrime
from time import time

s = time()
def rightprime(n):
    n = str(n)
    for i in range(len(n)):
        if not isPrime(int(n[i:])):
            return False
    return True
bidirection=[]
left={1:['2','3','5','7']}
layer = 1
while len(bidirection) <= 11 :
    nextlayer = layer+1
    left[nextlayer] = []
    for i in left[layer]:
        for j in [1,3,7,9]:
            number = i+str(j)
            if isPrime(int(number)):
                left[nextlayer].append(number)
                if rightprime(number):
                    bidirection.append(int(number))
    layer = nextlayer
    if left[layer]==[]:
        print('stop at',layer)
        break
print(bidirection)
print(sum(bidirection))
print(time()-s)

#%% another

s = time()

bidirection=[]
left={1:['2','3','5','7']}
right = {1:['3','7']}
layer = 1
while len(bidirection) <= 11 :
    nextlayer = layer+1
    left[nextlayer] = []
    right[nextlayer] = []
    for i in right[layer]:
        for j in range(1,10):
            number = str(j)+i
            if isPrime(int(number)):
                right[nextlayer].append(number)
    for i in left[layer]:
        for j in [1,3,7,9]:
            number = i+str(j)
            if isPrime(int(number)):
                left[nextlayer].append(number)
                if number in right[nextlayer]:
                    bidirection.append(int(number))
    layer = nextlayer
    if left[layer]==[] or right[layer] == []:
        print('stop at',layer)
        break
print(bidirection)
print(sum(bidirection))
print(time()-s)