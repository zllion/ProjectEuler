# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 12:11:28 2020

@author: zhixia liu
"""

"""
Project Euler 6: Sum square difference

The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

#%% naive

def dif(n):
    s1 = 0
    s2 = 0
    for i in range(n+1):
        s1 += (i)**2
        s2 += i
    s2 = s2**2
    return s2-s1
print(dif(100))
