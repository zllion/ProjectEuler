# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:44:31 2020

@author: zhixia liu
"""

"""
Project Euler 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#%% naive

def ispalindrome(n):
    n=str(n)
    for i in range(len(n)//2):
        if n[i]==n[-i-1]:
            continue
        else:
            break
    else:
        return True
    return False
def largestproduct():
    largest = 0
    for x in range(999,99,-1):
        for y in range(999,99,-1):
            p = x*y
            if ispalindrome(p):
                largest = max(largest,p)
    return largest

print(largestproduct())