# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 11:48:19 2020

@author: zhixia liu
"""

"""
Project Euler 19: Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

#%% naive

total_days = 101*365+100/4-1

n=366
y=1901
m=1
monthfirst = []
while y<=2000:
    monthfirst.append(n)
    if m in [1,3,5,7,8,10,12]:
        n += 31
        if m != 12:
            m+=1
        else:
            m=1
            y+=1
    elif m in [4,6,9,11]:
        n += 30
        m += 1
    else:
        if y%4 == 0 and y%400 != 0:
            n += 29
        else:
            n += 28
        m+=1
    print((n,m,y))
print(sum([n%7==0 for n in monthfirst]))  
