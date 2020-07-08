# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:48:03 2020

@author: zhixia liu
"""

"""
Project Euler 102

Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.

"""

def TwoPointLine(x1,y1,x2,y2):
    A= y1-y2
    B= -(x1-x2)
    C=x1*y2-x2*y1
    return A,B,C

def OrigininTriangle(x1,y1,x2,y2,x3,y3):
    A,B,C=TwoPointLine(x1,y1,x2,y2)
    if (A*x3+B*y3+C)*C<0:
        return False
    A,B,C=TwoPointLine(x2,y2,x3,y3)
    if (A*x1+B*y1+C)*C<0:
        return False
    A,B,C=TwoPointLine(x3,y3,x1,y1)
    if (A*x2+B*y2+C)*C<0:
        return False
    return True

if __name__ == '__main__':
    with open('p102_triangles.txt','r') as f:
        count = 0
        for line in f:
            triangle = [int(i) for i in line.strip().split(',')]
            if OrigininTriangle(*triangle):
                count += 1
    print(count)
    