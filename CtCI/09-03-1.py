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
        if value < mid:
            return self.findMagicIter(A, mid+1, end)
        else: # value > mid
            return self.findMagicIter(A, start, mid-1)
