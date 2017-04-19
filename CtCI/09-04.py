# -*- coding:utf-8 -*-
import copy
class Subset:
    # 返回二维[[],[],[]]
    def getSubsetsIter(self, A, n):
        # write code here
        if n == 0:
            return [[]]
        subSet = self.getSubsetsIter(A[:n-1],n-1)
        appededSets = copy.deepcopy(subSet)
        map(lambda elem: elem.append(A[-1]), appededSets)
        subSet.extend(appededSets)
        return subSet

    def getSubsets(self, A, n):
        res = self.getSubsetsIter(A, n)
        res = res[1:]
        res.reverse()
        map(lambda arr:arr.reverse(), res)
        return res
    

if __name__ == '__main__':
    print Subset().getSubsets([0,1], 2)