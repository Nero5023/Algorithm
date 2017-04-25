# -*- coding:utf-8 -*-

class MaxSum:
    def getMaxSum(self, A, n):
        # write code here
        arr = A
        maxSum = arr[0]
        start = 0
        end = 0
        for index in range(1,len(arr)):
            val = arr[index]
            if val <= 0:
                if maxSum < val:
                    maxSum = val
                    start = index
                    end = index
                    continue
                else:
                    continue
            # val > 0
            copyStart = start
            for i in range(copyStart, index+1):
                sumVal = sum(arr[i:index+1])
                if sumVal > maxSum:
                    maxSum = sumVal
                    start = i
                    end = index
        return maxSum

if __name__ == '__main__':
    print MaxSum().getMaxSum([-56,7,-129,-71,3,-119],6)
