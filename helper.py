# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:57:02 2020

@author: zhixia liu
"""
from math import sqrt
import itertools
import operator as op
from functools import reduce
import numpy as np


def gcd(p,q):
    if q == 0:
        return p
    p ,q = q, p%q
    return gcd(p,q)

def reducefrac(n,d):
    c = gcd(n,d)
    return (n//c,d//c)
    
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom
    
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def isSquare(n):
    return int(sqrt(n))**2 == n

def primefactor(n):
    # number must be even
    pf = []
    if n%2 == 0:
        pf.append(2)
    while n % 2 == 0:
        n = n//2
    # number must be odd
    for i in range(3, int(sqrt(n)) + 1, 2):
        if i > n:
            break
        if n%i == 0:
            pf.append(i)
        while n % i == 0:
            n = n // i
    # prime number greator than two
    if n > 2:
        pf.append(n)
    return pf

def coprime(n):
    pf = primefactor(n)
    sieve = [False]*n
    for p in pf:
        for i in range(p-1,n,p):
            sieve[i] = True
    return [j+1 for j,i in enumerate(sieve) if not i]

def totient(n):
    result = n
    if n%2 == 0:
        result -= result//2
    while n % 2 == 0:
        n = n//2
    # number must be odd
    for i in range(3, int(sqrt(n)) + 1, 2):
        if i > n:
            break
        if n%i == 0:
            result -= result//i
        while n % i == 0:
            n = n // i
    # prime number greator than two
    if n > 2:
        result -= result // int(n)
    return result
    
    
def maxPrimeFactor(n):
   # number must be even
    while n % 2 == 0:
        max_Prime = 2
        n /= 2
    # number must be odd
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            max_Prime = i
            n = n / i
    # prime number greator than two
    if n > 2:
        max_Prime = n
    return int(max_Prime)



def EratisthenesSieve(limit):
    crosslimit = int(sqrt(limit))
    sieve = [False]*limit
    sieve[0]=True
    for i in range(3,limit,2):
        sieve[i] = True
    for i in range(2,crosslimit,2):
        if not sieve[i]:
            for j in range(i*i+2*i,limit,2*i+2):
                sieve[j] = True
    return [i+1 for i in range(limit) if not sieve[i]]


def divisor(n): # self (n) not included
    divisorlst = [1]
    for j in range(2,int(sqrt(n))+1):
        if n%j == 0:
            divisorlst.append(j)
            if n//j > j:
                divisorlst.append(n//j)
    return divisorlst

class prime_list():
    def __init__(self,initiallize_limit = 1000):
        self.primelst = [2]
        self.n = 1
        self.initiallized = False
        self.initiallize_limit = initiallize_limit
        self.initiallize()
        
    def initiallize(self):
        if not self.initiallized:
            self.primelst = EratisthenesSieve(self.initiallize_limit)
            self.n = len(self.primelst)
            self.initiallized = True
            print('initialized')
        
    def generateToNth(self,n):
        while self.n<n:
            self.increment()
    
    def generateToN(self,n):
        while self.primelst[-1] < n:
            self.increment()

    def increment(self):
        candidate = self.primelst[-1]+1
        while True:
            if self.isPrime(candidate):
                self.primelst.append(candidate)
                self.n+=1
                return
            candidate += 1
            
    def isPrime(self,n):
        if n<self.primelst[-1]:
            return n in self.primelst
        limit = int(sqrt(n))
        self.generateToN(limit)
        for p in self.primelst:
            if p>limit:
                break
            if (n % p) == 0:
                return False
        return True
    
    def __getitem__(self,sliced):
        if isinstance(sliced,int):
            n = sliced
        else:
            n = sliced.stop
        if n is None: return self.primelst[sliced]
        if n>=self.n:
            print('expand')
            self.generateToNth(n+1)
        return self.primelst[sliced]
    
    def __iter__(self):
        return iter(self.primelst)

#%% continuous fraction
def sqrcf(N):
    m = 0
    d = 1
    sqr = int(sqrt(N))
    a = sqr
    if a**2 == N:
        return []
    l = [a]

    while a != 2*sqr:
        m = d*a - m
        d = (N-m**2)//d
        a = (sqr + m)//d
        l.append(a)
    
    return l



#%% triangle

def triangleareaHeron(a,b,c):
    s = (a+b+c)/2
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    return A

#%% sudoku

class SudokuSolver():
    
    def __init__(self,sudo):
        self.sudo = np.copy(sudo)
        self.empty = np.argwhere(sudo==0)
        self.currentpointer = 0
        self.setpointer()
    
    def setpointer(self):
        self.pointer = tuple(self.empty[self.currentpointer])
    
    def search(self):
        while self.currentpointer < len(self.empty):
            self.setpointer()
            while self.sudo[self.pointer] < 9:
                self.sudo[self.pointer] += 1
                if self.checkvalidity():
                    self.currentpointer += 1
                    break
            else:
                self.sudo[self.pointer] = 0
                self.currentpointer -= 1
        return self.sudo
    
    def checkvalidity(self):
        i,j = self.pointer
        n = self.sudo[self.pointer]
        if (n in self.sudo[i,:j]) or (n in self.sudo[i,j+1:]):
            return False
        elif (n in self.sudo[:i,j]) or (n in self.sudo[i+1:,j]):
            return False
        else:
            ii = i//3
            jj = j//3
            rg = [(x,y) for x in range(ii*3,ii*3+3) for y in range(jj*3,jj*3+3)]
            rg.remove((i,j))
            return not any([n == self.sudo[ind] for ind in rg])
        


