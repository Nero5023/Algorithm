from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        dicS = defaultdict(int)
        dicT = defaultdict(int)
        for x in s:
            dicS[x] += 1
        for x in t:
            dicT[x] += 1
        return dicS == dicT