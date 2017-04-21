# -*- coding:utf-8 -*-

class Finder:
    def findElement(self, mat, n, m, x):
        # write code here
        return self.findElementIter(mat, 0, 0, n-1, m-1, x)


    def findElementIter(self, mat, xStart, yStart, xEnd, yEnd, target):
        if xStart > xEnd or yStart > yEnd:
            return None
        rightTop = mat[xStart][yEnd]
        if rightTop == target:
            return [xStart, yEnd]
        if rightTop < target:
            return self.findElementIter(mat, xStart+1, yStart, xEnd, yEnd, target)
        else:
            return self.findElementIter(mat, xStart, yStart, xEnd, yEnd-1, target)

if __name__ == '__main__':
    print Finder().findElement([[1,2,3],[4,5,6]],2,3,6)