# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.guessIter(1, n)

    def guessIter(self, low, high):
        if low == high:
            return low
        mid = (low + high)/2
        res = guess(mid)
        if res == 0:
            return mid
        elif res == -1:
            return self.guessIter(low, mid-1)
        else:
            return self.guessIter(mid+1,high)