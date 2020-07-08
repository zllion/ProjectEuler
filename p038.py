# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:12:05 2020

@author: zhixia liu
"""

"""
Project Euler 38: Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

#%% naive

for i in range(1,10000):
    productacc = ''
    for j in range(1,10):
        productacc += str(i*j)
        if len(productacc)>9:
            break
        elif len(productacc)==9:
            if ''.join(sorted(productacc))=='123456789':
                print(productacc)
            break
