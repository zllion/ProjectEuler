# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:05:02 2020

@author: zhixia liu
"""

"""
Project Euler 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

#%% 

engnumbers = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
              8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
              14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
              19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
              70:'seventy',80:'eighty',90:'ninety'}
numberlen = {k:len(v) for k,v in engnumbers.items()}

length = 0
for i in range(1,1001):
    if i//1000>0:
        length += numberlen[i//1000]+8
        if i%1000 == 0:
            continue
    if i//100 > 0:
        length += numberlen[i//100]+7
        if i%100 == 0:
            continue
        length += 3
        i = i%100
    if i in numberlen:
        length += numberlen[i]
        continue
    length += numberlen[i-i%10] + numberlen[i%10]
print(length)
    
    
