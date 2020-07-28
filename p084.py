# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:44:09 2020

@author: zhixia liu
"""
"""
Project Euler Monopoly odds:
    
In the game, Monopoly, the standard board is set up in the following way:

GO	A1	CC1	A2	T1	R1	B1	CH1	B2	B3	JAIL
H2	 	C1
T2	 	U1
H1	 	C2
CH3	 	C3
R4	 	R2
G3	 	D1
CC3	 	CC2
G2	 	D2
G1	 	D3
G2J	F3	U2	F2	F1	R3	E3	E2	CH2	E1	FP
A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.

Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

"""

#%% naive
import matplotlib.pyplot as pyplt
import numpy as np
from random import randint
class monopoly():
    def __init__(self):
        self.currentsquare=0
        self.squarecounts = np.zeros(40)
        self.consecutivedoubles=0
        self.dices=(0,0)
        self.dicedigit = 6
    
    def throwdices(self):
        self.dices=(randint(1,self.dicedigit),randint(1,self.dicedigit))
        return
    
    def advances(self):
        self.throwdices()
        self.currentsquare += sum(self.dices)
        self.currentsquare %= 40
        if self.dices[0] == self.dices[1]:
            self.consecutivedoubles += 1
        else:
            self.consecutivedoubles = 0
        self.cast()
        self.squarecounts[self.currentsquare] += 1
        return
    
    def cast(self):
        if self.consecutivedoubles == 3:
            self.currentsquare = 10
            self.consecutivedoubles == 0
            return
        if self.currentsquare == 30:
            self.currentsquare = 10
            return
        if self.currentsquare in [2,17,33]:
            self.drawcc()
            return
        if self.currentsquare in [7,22,37]:
            self.drawch()
            return
        
    def drawcc(self):
        card = randint(1,16)
        if card == 1:
            self.currentsquare=0
        if card == 2:
            self.currentsquare=10
        return
    
    def drawch(self):
        card=randint(1,16)
        if card == 1:
            self.currentsquare = 0
        elif card == 2:
            self.currentsquare = 10
        elif card == 3:
            self.currentsquare = 11
        elif card == 4:
            self.currentsquare = 24
        elif card == 5:
            self.currentsquare = 39
        elif card == 6:
            self.currentsquare = 5
        elif card == 7:
            self.nextR()
        elif card == 8:
            self.nextR()
        elif card == 9:
            self.nextU()
        elif card == 10:
            self.currentsquare -= 3
        return
    
    def nextR(self):
        for i in [5,15,25,35]:
            if i > self.currentsquare:
                self.currentsquare = i
                break
        else:
            self.currentsquare = 5
        return
    
    def nextU(self):
        for i in [12,28]:
            if i > self.currentsquare:
                self.currentsquare = i
                break
        else:
            self.currentsquare = 12
        return
    
    def statistic(self,loop):
        for i in range(loop):
            self.advances()
        return self.squarecounts
    
    def top3(self):
        return sorted([(i,v) for i,v in enumerate(self.squarecounts)], key=lambda x: x[1],reverse = True)[:3]
game = monopoly()
loop = 500000
game.dicedigit = 4
result = game.statistic(loop)
pyplt.bar(range(40),result/loop)
pyplt.show()
print(game.top3())