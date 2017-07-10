class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return C(m+n-2, n-1)

def factorial(n):
    res = reduce(lambda acc, x: acc*x, range(1, 1+n), 1)
    return res


def C(n,m):
    return factorial(n)/(factorial(m)*factorial(n-m))

if __name__ == '__main__':
    s = Solution()
    print s.uniquePaths(1,10)