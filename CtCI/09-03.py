# -*- coding:utf-8 -*-
class MagicIndex:
    def findMagicIndex(self, A, n):
        # write code here
        return self.findMagicIndexIter(A, 0, n-1)

    def findMagicIndexIter(self, arr, start, end):
        if start > end:
            return False
        mid = start + (end-start)//2
        value = arr[mid]
        if value == mid:
            return True
        if value > mid:
            return self.findMagicIndexIter(arr, start, mid-1)
        else:
            return self.findMagicIndexIter(arr,mid+1, end)



if __name__ == '__main__':
    print MagicIndex().findMagicIndex([1,3,4,5,6], 5)