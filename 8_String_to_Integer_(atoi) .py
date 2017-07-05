class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "":
            return 0
        if str[0] == "-":
            res = self.myAtoi(str[1:])
            return -1*res
        if str[0] == "+":
            return self.myAtoi(str[1:])
        higher = str[:len(str)-1]
        higherNum = self.myAtoi(higher)
        last = str[-1]
        try:
            lastNum = int(last)
        except:
            return higherNum
        else:
            return higherNum*10 + lastNum
