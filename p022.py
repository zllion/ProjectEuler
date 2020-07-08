# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:20:28 2020

@author: zhixia liu
"""

"""
Project Euler 22: Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
#%% naive
with open('p022_names.txt','r') as f:
    names = sorted([name[1:-1] for name in f.readline().split(',')])

def namescore(name):
    return sum([ord(c)-64 for c in name])

print(sum([namescore(name)*(n+1) for n,name in enumerate(names)]))
        