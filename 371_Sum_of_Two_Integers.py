class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        if b == 0:
            return a
        if negate(a) == b:
            return 0

        sumWithoutCarry = a^b
        carry = (a&b) << 1
        # if (sumWithoutCarry == self.getSum(a,a) and carry == self.getSum(b,b)) or \
        #     (sumWithoutCarry == self.getSum(b,b) and carry == self.getSum(a,a)):
        #     if sumWithoutCarry != carry:
        #         return 0
        return self.getSum(sumWithoutCarry, carry)

def negate(x):
    return ~x+1

if __name__ == '__main__':
    s = Solution()
    print s.getSum(-16,14)
    # print negate(3)