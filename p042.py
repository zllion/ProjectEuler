# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:57:29 2020

@author: zhixia liu
"""

"""
Project Euler 42: Coded triangle numbers

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

#%% naive

with open('p042_words.txt','r') as f:
    words = [w[1:-1] for w in f.readline().strip().split(',')]

triangle = [n*(n+1)/2 for n in range(1,50)]
def isTriangle(w):
    s = sum([ord(c)-64 for c in w])
    return (s in triangle)
s=0
for w in words:
    if isTriangle(w.strip()):
        s += 1
print(s)