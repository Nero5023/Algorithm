class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        absNum = abs(num)
        res = ""
        if absNum == 0:
            return "0"
        while absNum != 0:
            temp = absNum%7
            res = str(temp) + res
            absNum /= 7
        if num < 0:
            res = "-" + res
        return res

if __name__ == '__main__':
    s = Solution()
    print s.convertToBase7(-7)
