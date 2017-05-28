from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sCoun = Counter(list(s))
        tCoun = Counter(list(t))
        tCoun.subtract(sCoun)
        for key in tCoun:
            if tCoun[key] != 0:
                return key
        

