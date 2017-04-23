# -*- coding:utf-8 -*-
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class Bipartition:
    def getBipartition(self, A, B):
        # write code here
        (xa, ya) = getMidPoint(A)
        (xb, yb) = getMidPoint(B)
        k = (ya-yb)/(1.0*(xa-xb))
        b = ya - k*xa
        return [k, b]


def getMidPoint(matrix):
    y = matrix[0][1] + matrix[1][1]
    y = y/2.0
    x = matrix[0][0] + matrix[3][0]
    x = x/2.0
    return (x,y) 

if __name__ == '__main__':
    print getMidPoint([(1,0),(1,1),(2,0),(2,1)])
    print Bipartition().getBipartition([(136,6278),(3958,6278),(3958,2456),(136,2456)],[(-3898,11132),(7238,11132),(7238,-4),(-3898,-4)])