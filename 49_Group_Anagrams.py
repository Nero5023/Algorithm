from collections import defaultdict
from itertools import permutations

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        keyMap = {}
        # for x in strs:
        #     if x in keyMap:
        #         key = keyMap[x]
        #         dic[key].append(x)
        #     else:
        #         for strlist in permutations(x):
        #             s = "".join(strlist)
        #             keyMap[s] = x
        #         dic[x].append(x)

        for x in strs:
            strarry = list(x)
            strarry.sort()
            key = ''.join(strarry)
            dic[key].append(x)
        
        res = []
        for x in dic:
            res.append(dic[x])
        print res
        return res

if __name__ == '__main__':
    s = Solution()
    s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])