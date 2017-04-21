class Solution(object):
    # this k is start from 1
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = numStr(n)
        return self.getPermutationIter(nums, k-1)

    # this k is start from 0
    def getPermutationIter(self, listStr, k):
        if len(listStr) == 1:
            return listStr[0]
        km1Fac = factorial(len(listStr)-1)
        index = k//km1Fac
        firstNum = listStr[index]
        remainListStr = removeIndex(listStr, index)
        remainStr = self.getPermutationIter(remainListStr, k%km1Fac)
        return firstNum + remainStr

def numStr(n):
    res = []
    iterNum = '1'
    for i in range(0, n):
        res.append(iterNum)
        iterNum = chr(ord(iterNum) + 1)
    return res


def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

def removeIndex(arr, index):
    return arr[:index] + arr[index+1:]

if __name__ == '__main__':
    print Solution().getPermutation(1,1)