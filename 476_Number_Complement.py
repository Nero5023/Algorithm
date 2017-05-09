class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binlen = len(bin(num)[2:])
        mask = 1 << binlen
        mask = mask - 1
        res = (~num) & mask
        return res

if __name__ == '__main__':
    s = Solution()
    print s.findComplement(5)
