# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:18:54 2020

@author: zhixia liu
"""

"""
Project Euler 68: Magic 5-gon ring

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?


"""

#%% naive bf

#assume sum to 70/5=14

inner = [1,2,3,4,5]
outer = [6,7,8,9,10]
results = []

s=14

def findnext(seq,s=14):
    if len(seq) == 12:
        rest = [i for i in outer if i not in seq][0]
        if  rest + seq[-1] + seq[1] == s:
            return [seq + [rest,seq[-1],seq[1]]]
        else:
            return []
    outerrest = [i for i in outer if i not in seq]
    innerrest = [i for i in inner if i not in seq]
    results = []
    for i in outerrest:
        for j in innerrest:
            if i+j+seq[-1] == s:
                newseq = seq + [i,seq[-1],j]
                results.extend(findnext(newseq,s))
    return results

print(findnext([6,5,3]))
print(findnext([6,3,5]))
