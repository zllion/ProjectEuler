# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:33:32 2020

@author: zhixia liu
"""

"""
Project Euler 51: Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

#%% naive bf

# at least 3 same digits 

from itertools import combinations
from helper import prime_list
from time import time

st = time()

family_dict={}

prime=prime_list(1000000)

for i in prime:
    if i <1000: continue
    label = str(i)
    for j in '0123456789':
        count = label.count(j)
        if count == 1:continue
        elif count == 2:
            family_dict.setdefault(label.replace(j,'*'),[]).append(i)
        elif count >= 3:
            full_indeces = [x for x,y in enumerate(label) if y==j]
            for d in range(2,count+1):
                for indeces in combinations(full_indeces,d):
                    templabel = label
                    for index in indeces:
                        templabel = templabel[:index]+'*'+templabel[index+1:]
                    family_dict.setdefault(templabel,[]).append(i)
    
seven = [(k,v) for k,v in family_dict.items() if len(v) == 7]
eight = [(k,v) for k,v in family_dict.items() if len(v) == 8]
print(seven)
print(eight)

print(time()-st)
