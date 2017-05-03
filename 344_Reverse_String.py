class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList = list(s)
        sList.reverse()
        return ''.join(sList)