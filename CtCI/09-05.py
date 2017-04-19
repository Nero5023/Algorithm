# -*- coding:utf-8 -*-
class Permutation:
    # A是一个字符串
    def getPermutation(self, A):
        # write code here
        listStr = list(A)
        listStr.reverse()
        res = self.getPermutationIter(listStr)
        res.sort(reverse=True)
        return res

    # give reverse str
    def getPermutationIter(self, listStr):
        if len(listStr) == 0:
            return [""]
        res = []
        copyStr = listStr[:]
        for i in range(0, len(listStr)):
            self.exchange(copyStr, i, len(listStr)-1)
            ch = copyStr.pop()
            strs = self.getPermutationIter(copyStr)
            strs = map(lambda s:ch+s,strs)
            res.extend(strs)
            copyStr = listStr[:]
        return res

    def exchange(self, s, i, j):
        temp = s[i]
        s[i] = s[j]
        s[j] = temp

if __name__ == '__main__':
    print Permutation().getPermutation("ABC")
