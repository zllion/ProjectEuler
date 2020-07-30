# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:17:55 2020

@author: zhixia liu
"""
"""
Project Euler 89: Roman numerals

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

#%% 

with open('p089_roman.txt','r') as f:
    roman = []
    for line in f:
        roman.append(line.strip())

r2n = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
n2r = {v:k for k,v in r2n.items()}

def roman2number(r):
    s = 0
    pre = float('inf')
    for i in r:
        n = r2n[i]
        if n <= pre:
            s += n
        else:
            s = s - 2*pre + n
        pre = n
    return s

def short(n):
    s=''
    for i in sorted(list(n2r.keys()),reverse=True):
        s += n2r[i]*(n//i)
        n = n%i
    s=s.replace('IIII','IV')
    s=s.replace('VIV','IX')
    s=s.replace('XXXX','XL')
    s=s.replace('LXL','XC')
    s=s.replace('CCCC','CD')
    s=s.replace('DCD','CM')
    return s


diff = [len(r)-len(short(roman2number(r))) for r in roman]
print(sum(diff))