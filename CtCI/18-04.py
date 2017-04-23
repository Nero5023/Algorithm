# -*- coding:utf-8 -*-

class Count2:
    def countNumberOf2s(self, n):
        dic = {}
        return self.countNumberOf2sCache(n, dic)
        # # write code here
        # numStr = str(n)
        # if len(numStr) == 1:
        #     if n >= 2:
        #         return 1
        #     else:
        #         return 0
        # remianNum = int(numStr[1:])
        # firstNum = int(numStr[0])
        # res0 = self.countNumberOf2s(remianNum)
        # maxRemainNum = 10**(len(numStr)-1) - 1
        # maxRemainRes = self.countNumberOf2s(maxRemainNum)

        # maxRemainRes = maxRemainRes*firstNum
        # if firstNum == 2:
        #     res0 += (remianNum+1)
        # if firstNum > 2:
        #     maxRemainRes += (maxRemainNum+1)
        # return res0 + maxRemainRes

    def countNumberOf2sCache(self, n, cache):
        # write code here
        if cache.get(n) is not None:
            return cache[n]
        numStr = str(n)
        if len(numStr) == 1:
            if n >= 2:
                return 1
            else:
                return 0
        remianNum = int(numStr[1:])
        firstNum = int(numStr[0])

        res0 = self.countNumberOf2s(remianNum)
        cache[remianNum] = res0

        maxRemainNum = 10**(len(numStr)-1) - 1

        maxRemainRes = self.countNumberOf2s(maxRemainNum)
        cache[maxRemainNum] = maxRemainRes

        maxRemainRes = maxRemainRes*firstNum
        if firstNum == 2:
            res0 += (remianNum+1)
        if firstNum > 2:
            maxRemainRes += (maxRemainNum+1)
        return res0 + maxRemainRes


if __name__ == '__main__':
    print Count2().countNumberOf2s(29)

