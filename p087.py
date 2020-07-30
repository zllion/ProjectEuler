# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:35:09 2020

@author: zhixia liu
"""
"""

Project Euler 87: Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

"""

#%% 

from itertools import product
from helper import prime_list



uplimit = 50000000
limit2 = int(uplimit**0.5)
limit3 = int(uplimit**(1/3))
limit4 = int(uplimit**0.25)

prime2 = prime_list(2)
prime3 = prime_list(2)
prime4 = prime_list(2)

prime2.generateToN(limit2)
prime3.generateToN(limit3)
prime4.generateToN(limit4)

totalset = set()

for i in [x**2 for x in prime2]:
    for j in [x**3 for x in prime3]:
        for k in [x**4 for x in prime4]:
            s = i + j + k
            if s < uplimit:
                totalset.add(s)

print(len(totalset))

