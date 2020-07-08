# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:46:56 2020

@author: zhixia liu
"""

"""
Project Euler 54:Poker hands
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

#%% 
value2number = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}
suit2number = {'H':0,'C':1,'S':2,'D':3}
def indeces(lst,v):
    return [i for i,j in enumerate(lst) if j==v][::-1]

def rank(cards):
    values = [0]*13
    suits = [0]*4
    for i in cards:
        values[value2number[i[0]]] += 1
        suits[suit2number[i[1]]] += 1
    if 5 in suits: 
        isflush = True
    else:
        isflush = False
    isstraight = False
    for i in range(9):
        if values[i] == 1:
                if values[i+1]*values[i+2]*values[i+3]*values[i+4]==1:
                    isstraight = True

    if not isflush:
        if values.count(1) == 5 and not isstraight: #high card
            return [0]+indeces(values,1)
        elif values.count(2) == 1 and values.count(3) == 0 : # 1 pair
            return [1] + indeces(values,2) + indeces(values,1)
        elif values.count(2) == 2 : # 2pairs
            return [2] + indeces(values,2) + indeces(values,1)
        elif values.count(3) == 1 and values.count(2) == 0 : # 3 of a kind
            return [3] + indeces(values,3) + indeces(values,1)
        elif isstraight: # straight
            return [4] + indeces(values,1)
        elif values.count(3) == 1 and values.count(2) == 1: # full house
            return [6] + indeces(values,3) + indeces(values,2)
        elif values.count(4) == 1: # 4 of a kind
            return [7] + indeces(values,4)
    else:
        if not isstraight: # flush
            return [5] + indeces(values,3)+indeces(values,2)+indeces(values,1)
        elif isstraight: #straight flush and royal flush, rank 8
            return [8]+indeces(values,1)
# p1='3C 3D 3S 9S 9D'.split()
# print(rank(p1))
def win(p1,p2):
    r1 = rank(p1)
    r2 = rank(p2)
    if r1==r2: print('tie')
    return r1>r2

# p1 = '2D 9C AS AH AC'.split()
# p2 = '3D 6D 7D TD QD'.split()
# print(win(p1,p2))
p1win = 0
with open('p054_poker.txt','r') as f:
    for line in f:
        cards = line.strip().split(' ')
        p1 = cards[:5]
        p2 = cards[5:]
        if win(p1,p2):
            p1win += 1
print(p1win)










