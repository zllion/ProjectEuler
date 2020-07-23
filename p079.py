# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:06:04 2020

@author: zhixia liu
"""

"""
Project Euler 79: Passcode derivation

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

#%% naive bf

with open('p079_keylog.txt','r') as f:
    code = set()
    for l in f:
        code.add(l.strip())
print(code)

def findindex(v,itr):
    return [i for i,e in enumerate(itr) if v==e ]

def strinsert(s,i,v):
    return s[:i]+v+s[i:]

def greedyinsert(code,key):
    
    candidate=[]
    
    



#%% by hand

n='73162890'    