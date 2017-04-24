# -*- coding:utf-8 -*-
from collections import defaultdict
class SortString:
    def sortStrings(self, s, n):
        dic = defaultdict(list)
        strToSort = []
        for x in s:
            sortedx = sorted(x)
            sortedx = ''.join(sortedx)
            if dic[sortedx] == []:
                strToSort.append(sortedx)
            dic[sortedx].append(x)
        strToSort.sort()
        res = []
        for x in strToSort:
            compareStrs = dic[x]
            compareStrs.sort()
            res.extend(compareStrs)
        return res

if __name__ == '__main__':
    print SortString().sortStrings(["ab","ba","abc","cba"], 2)