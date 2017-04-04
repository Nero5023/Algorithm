class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if stones[1] - stones[0] != 1:
            return False

        N = len(stones)
        res = self.calculateDP(stones)

        # print res
        return len(res[N-1]) != 0


    def calculateDP(self, stones):
        N = len(stones)
        dp = [set() for _ in range(0, N)]
        dp[1].add(stones[1] - stones[0])
        for m in range(2, N):
            for n in range(1, m):
                self.calculateDPIter(n, m, dp, stones)
        return dp




# from n to m
    def calculateDPIter(self, n, m, dp, stones):
        if n >= m:
            return
        else:
            if len(dp[n]) == 0:
                return
            stride = stones[m] - stones[n]
            if (stride in dp[n]) or ((stride-1) in dp[n]) or ((stride+1) in dp[n]):
                dp[m].add(stride)

if __name__ == '__main__':
    s = Solution()
    print s.canCross([0,1,3,5,6,8,12,17])
    print s.canCross([0,1,2,3,4,8,9,11])

    # print s.canCross([0,1])
