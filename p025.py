# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:19:18 2020

@author: zhixia liu
"""

"""
Project Euler 25: 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

#%% naive

fibonaccilst = {1:1,2:1}
def fibonacci(n):
    if n <= len(fibonaccilst):
        return fibonaccilst[n]
    else:
        fibonaccilst[n] = fibonacci(n-1) + fibonacci(n-2)
        return fibonaccilst[n]

n=1
l=1
while l<1000:
    n+=1
    f = fibonacci(n)
    l=len(str(f))
print(f)
print(n)

