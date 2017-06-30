class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.hammingWeightIter(n,0)
    
    def hammingWeightIter(self, n, res):
        if n == 0:
            return res
        else:
            temp = n & (n-1)
            return self.hammingWeightIter(temp, res+1)
