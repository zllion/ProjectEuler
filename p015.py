# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:51:53 2020

@author: zhixia liu
"""

"""
Project Euler 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

"""

#%% naive
from scipy.special import comb
print(comb(40,20,exact=True))