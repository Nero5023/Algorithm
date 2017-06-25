from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordsFre = defaultdict(int)
        visited = defaultdict(int)
        for x in s:
            wordsFre[x] += 1
        res = []
        for x in s:
            wordsFre[x] -= 1
            if visited[x]:
                continue
            while len(res) != 0 and wordsFre[res[-1]] != 0 and x < res[-1]:
                visited[res[-1]] = 0
                res.pop()
            res.append(x)
            visited[x] = 1
        return ''.join(res)

if __name__ == '__main__':
    s = Solution()
    print s.removeDuplicateLetters("cbacdcbc")