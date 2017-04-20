# -*- coding:utf-8 -*-

def dividorNum5(x):
    res = 0
    while x % 5 == 0:
        res += 1
        x /= 5
    return res

class Factor:
    def getFactorSuffixZero(self, n):
        # write code here
        res = 0
        for num in range(5, n+1, 5):
            res += dividorNum5(num)
        return res

if __name__ == '__main__':
    print Factor().getFactorSuffixZero(25)