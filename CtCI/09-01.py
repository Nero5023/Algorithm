# -*- coding:utf-8 -*-
class GoUpstairs:
    def countWays(self, n):
        # write code here
        cache = {}
        return countWaysIter2(n)

def countWaysIter(n, cache):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if cache.get(n) is not None:
        return cache[n]
    res = countWaysIter(n-1, cache)%1000000007 + countWaysIter(n-2, cache)%1000000007 + countWaysIter(n-3, cache)%1000000007
    cache[n] = res
    return res

def countWaysIter2(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    x1 = 1
    x2 = 2
    x3 = 4
    res = 0
    for i in range(4, n+1):
        res = (x1 + x2 + x3)%1000000007
        x1 = x2
        x2 = x3
        x3 = res
    return res
if __name__ == '__main__':
    print GoUpstairs().countWays(36196)