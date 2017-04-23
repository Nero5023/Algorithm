# -*- coding:utf-8 -*-
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

class Robot:
    def countWays(self, x, y):
        # write code here
        return nCr(x+y-2, x-1)


print nCr(2,1)