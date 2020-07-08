# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:27:51 2020

@author: zhixia liu
"""

"""
Project Euler 50: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""

#%% naive bf

from helper import prime_list
from time import time
from tqdm import tqdm
from math import sqrt

prime = prime_list(100000)
st=time()


st=time()
end_ini = 2
def isConsecutiveSum(n):
    start = 0
    global end_ini
    end = end_ini
    s = sum(prime[start:end])
    while s<n:
        s += prime[end]
        end+=1
    end_ini = end
    while end - start > 1:
        if s==n:
            return [start,end]
        elif s<n:
            s += prime[end]
            end += 1
        else:
            s -= prime[start]
            start += 1
    return []

results=[]
maxseq={'number':0,'len':0}
for i in tqdm(prime):
    result = isConsecutiveSum(i)
    if result!=[]:
        results.append(result)
        if result[1]-result[0]>maxseq['len']:
            maxseq['number'],maxseq['len']=i,result[1]-result[0]
print(results[-10:])
print(maxseq)
print(time()-st)

#%% improved
mm = 1000000
prime = prime_list(mm)


st=time()
def search():
    maxn=2
    s = sum(prime[:2])
    while s<mm:
        s += prime[maxn]
        maxn+=1
    maxseq={'number':0,'len':0}
    s = sum(prime)
    for i in range(prime.n-maxn,prime.n):
        tempsum=s-sum(prime[:i])
        for j in range(i):
            start = i-1-j
            end = prime.n-1-j
            tempsum = tempsum +prime[start]-prime[end]
            if tempsum > mm: continue
            if prime.isPrime(tempsum):
                maxseq['number'] = tempsum
                maxseq['len'] = end-start
                return maxseq
print(search())
print(time()-st)