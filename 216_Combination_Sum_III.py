class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = self.combinationSum3Iter(k,n,0)
        if res == None:
            return []
        return res

    def combinationSum3Iter(self, k, n, minValue):
        if k == 0 and n == 0:
            return [[]]
        if k == 0 and n != 0:
            return None
        if sumFrom(minValue+1, min(9,k)) > n:
            return None
        res = []
        for x in range(minValue+1, min(10,n+1)):
            comSum = self.combinationSum3Iter(k-1, n-x, x)
            if comSum is not None:
                map(lambda xs:xs.append(x), comSum)
                res.extend(comSum)
        return res



def sumFrom(x, k):
    return sum(range(x,x+k))

if __name__ == '__main__':
    s = Solution()
    print s.combinationSum3(5,18)