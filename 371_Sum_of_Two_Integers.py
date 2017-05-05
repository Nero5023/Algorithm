class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        if b != 0:
            sumWithoutCarry = a^b
            carry = (a&b) << 1
            return self.getSum(sumWithoutCarry, carry)
        return a

if __name__ == '__main__':
    s = Solution()
    s.getSum(-1,1)