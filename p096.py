# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:40:54 2020

@author: zhixia liu
"""
"""
Project Euler 96: Su Doku

Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

p096_1.png     p096_2.png
A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.
"""

#%% naive backtracking
import numpy as np
from tqdm import tqdm

sudoku = []

with open('p096_sudoku.txt','r') as f:
    for line in f:
        if line.startswith('Grid'):
            m=np.zeros((9,9),dtype=np.int32)
            i=0
            continue
        n = [int(i) for i in line.strip()]
        m[i,:] = np.array(n,dtype=np.int32)
        i+=1
        if i == 9:
            sudoku.append(m)
    
class SudokuSolver():
    
    def __init__(self,sudo):
        self.sudo = np.copy(sudo)
        self.empty = np.argwhere(sudo==0)
        self.currentpointer = 0
        self.setpointer()
    
    def setpointer(self):
        self.pointer = tuple(self.empty[self.currentpointer])
    
    def search(self):
        while self.currentpointer < len(self.empty):
            self.setpointer()
            while self.sudo[self.pointer] < 9:
                self.sudo[self.pointer] += 1
                if self.checkvalidity():
                    self.currentpointer += 1
                    break
            else:
                self.sudo[self.pointer] = 0
                self.currentpointer -= 1
        return self.sudo
    
    def checkvalidity(self):
        i,j = self.pointer
        n = self.sudo[self.pointer]
        if (n in self.sudo[i,:j]) or (n in self.sudo[i,j+1:]):
            return False
        elif (n in self.sudo[:i,j]) or (n in self.sudo[i+1:,j]):
            return False
        else:
            ii = i//3
            jj = j//3
            rg = [(x,y) for x in range(ii*3,ii*3+3) for y in range(jj*3,jj*3+3)]
            rg.remove((i,j))
            return not any([n == self.sudo[ind] for ind in rg])
        
            
    
# solver= SudokuSolver(sudoku[0])
# print(solver.search())
            
s = 0
for sudo in tqdm(sudoku):
    s += sum(SudokuSolver(sudo).search()[0,:3]*[100,10,1])
    print(s)
