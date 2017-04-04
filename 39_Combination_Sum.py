class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort(reverse=True)
        res = self.combinationSumRe(candidates, target)
        if res is None:
            return []
        return res
    
    def combinationSumRe(self, candidates, target):
        """
        candidates is sorted
        """
        if target == 0:
            return [[]]
        if target < 0:
            return None
        candidates = filter(lambda x: x<=target, candidates)
        if len(candidates) == 0:
            return None
        res = []
        # for x in candidates:
        for index, x in enumerate(candidates):
            innerRes = self.combinationSumRe(candidates[index:], target-x)
            if innerRes is None:
                continue
            # innerRes = map(lambda lis: lis.append(x), innerRes)
            for a in innerRes:
                a.append(x)
            res.extend(innerRes)
        return res

if __name__ == '__main__':
    so = Solution()
    print(so.combinationSum([2,3,6,7], 7))