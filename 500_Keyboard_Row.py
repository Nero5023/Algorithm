class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        chars = ['qwertyuiop','asdfghjkl','zxcvbnm']
        dic = {}
        for i in range(3):
            for ch in chars[i]:
                dic[ch] = i
        def reduceIter(acc, x):
            if acc[0] == False:
                return (False, None)
            # acc[0] = True
            if acc[1] is None or dic[x] == acc[1]:
                return (True, dic[x])
            else:
                return (False, None)

        def isInSameLine(word):
            res = reduce(reduceIter, word.lower(), (True, None))
            return res[0]
        return filter(isInSameLine, words)

if __name__ == '__main__':
    s = Solution()
    print s.findWords(["Hello","Alaska","Dad","Peace"])