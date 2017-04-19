# -*- coding:utf-8 -*-
class MagicIndex:
    def findMagicIndex(self, A, n):
        # write code here
        return self.findMagicIter(A, 0, n-1)

    def findMagicIter(self, A, start, end):
        if start > end:
            return False
        mid = (start+end)//2
        value = A[mid]
        if value == mid:
            return True
        left = right = False

        # if value < mid:
        #     left = self.findMagicIter(A, start, value)
        #     right = self.findMagicIter(A, mid+1, end)
        # else:
        #     left = self.findMagicIter(A, start, mid-1)
        #     right = self.findMagicIter(A, value, end)
        # if left == False and right == False:
        #     return False
        # else:
        #     return True

        leftIndex = min(mid-1,value)
        left = self.findMagicIter(A, start, leftIndex)
        if left == True:
            return True
        rightIndex = max(mid+1, value)
        right = self.findMagicIter(A, rightIndex, end)
        return right


if __name__ == '__main__':
    print MagicIndex().findMagicIndex([1,1,3,4,5], 5)