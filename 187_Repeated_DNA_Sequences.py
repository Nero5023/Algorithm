from collections import defaultdict
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = defaultdict(int)
        for i in range(0, len(s)-9):
            sub = s[i:i+10]
            dic[sub] += 1
        res = []
        for key in dic:
            if dic[key] > 1:
                res.append(key)
        return res


