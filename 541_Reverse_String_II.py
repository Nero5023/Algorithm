class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        splitStrs = [s[i:i+2*k] for i in range(0, len(s),2*k)]
        res = map(reverseHalf(k), splitStrs)
        return "".join(res)


def reverseHalf(k):
    def innerFunc(s):
        if len(s) <= k:
            return s[::-1]
        firstK = s[:k][::-1]
        return firstK + s[k:]
    return innerFunc