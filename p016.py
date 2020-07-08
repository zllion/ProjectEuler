# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:58:46 2020

@author: zhixia liu
"""

"""
Project Euler 16: Power digit sum

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

#%% naive

print(sum([int(i) for i in str(2**1000)]))