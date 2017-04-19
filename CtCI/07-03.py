# -*- coding:utf-8 -*-

class Finder:
    def findElement(self, A, n, x):
        # write code here
        return self.findElementIter(A, 0, n-1, x)

    def findElementIter(self, arr, start, end, target):
        if start > end:
            return None
        mid = (start+end)//2
        value = arr[mid]
        if (value == target):
            return mid
        if (target > value): # on the right
            if arr[mid] > arr[end]:
                return self.findElementIter(arr, mid+1, end, target)
            elif arr[mid] < arr[end]:
                right = self.findElementIter(arr, mid+1, end, target)
                left  = self.findElementIter(arr, start, mid-1, target)
                if right is None and left is None:
                    return None
                elif right is None:
                    return left
                else:
                    return right
            else:
                return None
        else:
            if arr[mid] < arr[end]:
                return self.findElementIter(arr, start, mid-1, target)
            elif arr[mid] > arr[end]:
                right = self.findElementIter(arr, mid+1, end, target)
                left  = self.findElementIter(arr, start, mid-1, target)
                if right is None and left is None:
                    return None
                elif right is None:
                    return left
                else:
                    return right
            else:
                return None

if __name__ == '__main__':
    print Finder().findElement([15,16,19,20,25,1,3,4,5,7,10,14],12,5)
