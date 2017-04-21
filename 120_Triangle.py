class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        cache = {}
        def getMinSumTo(triangle, row, col):
            if col < 0 or col > row:
                return None
            if row == 0:
                return triangle[0][0]
            key = (row, col)
            if key in cache:
                return cache[key]
            x1 = getMinSumTo(triangle, row-1, col)
            x2 = getMinSumTo(triangle, row-1, col-1)
            res = 0
            if x1 is not None and x2 is not None:
                res = min(x1, x2)
            if x1 is None:
                res = x2
            if x2 is None:
                res = x1
            # print row, col
            res += triangle[row][col]
            cache[(row, col)] = res
            return res
        maxRow = len(triangle)-1
        res = getMinSumTo(triangle, maxRow, 0)
        for i in range(1, maxRow+1):
            res = min(res, getMinSumTo(triangle, maxRow, i))
        return res

if __name__ == '__main__':
    s = Solution()
    print s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])