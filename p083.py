# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:43:32 2020

@author: zhixia liu
"""
"""
Project Euler 83: Path sum: four ways

NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

 
Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

#%% naive
from time import time
import numpy as np

m=np.loadtxt(open('p083_matrix.txt', "rb"), delimiter=",", skiprows=0)
limit_i,limit_j = m.shape


minipath = np.zeros(m.shape)
visited = np.zeros(m.shape)
visited[0,0] = 1
minipath[0,0] = m[0,0]
def activateneighbour(node):
    neighbour=[]
    i = node[0]
    j = node[1]
    if i > 0 and visited[i-1,j] == 0:
        nextnode = (i-1,j)
        neighbour.append((nextnode,minipath[node]+m[nextnode]))
        visited[nextnode] = 1
    if j > 0 and visited[i,j-1] == 0:
        nextnode = (i,j-1)
        neighbour.append((nextnode,minipath[node]+m[nextnode]))
        visited[nextnode] = 1
    if i < limit_i-1 and visited[i+1,j] == 0:
        nextnode = (i+1,j)
        neighbour.append((nextnode,minipath[node]+m[nextnode]))
        visited[nextnode] = 1
    if j < limit_j-1 and visited[i,j+1] == 0:
        nextnode = (i,j+1)
        neighbour.append((nextnode,minipath[node]+m[nextnode]))
        visited[nextnode] = 1
    return neighbour

neighbours=activateneighbour((0,0))
while neighbours:
    nextnode = min(neighbours,key=lambda x: x[1])
    # print(nextnode)
    neighbours.remove(nextnode)
    minipath[nextnode[0]]=nextnode[1]
    neighbours.extend(activateneighbour(nextnode[0]))
    # print('next')

print(minipath[-1,-1])
