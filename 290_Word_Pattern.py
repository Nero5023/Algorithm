class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dic = {}
        dic2 = {}
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        for (index, x) in enumerate(pattern):
            if x in dic:
                if dic[x] != words[index]:
                    return False
            else:
                if words[index] in dic2:
                    return False
                dic2[words[index]] = x
                dic[x] = words[index]
        return True