# -*- coding:utf-8 -*-
class Coins:
    def countWays(self, n):
        # write code here
        return self.contWaysIter(n, [25,10,5,1])

    def contWaysIter(self, money, coins):
        if money < 0:
            return 0;
        if money == 0:
            return 1
        if coins[0] == 1:
            return 1
        i = 0
        res = 0
        while money - i*coins[0] >= 0:
            res += self.contWaysIter(money - i*coins[0], coins[1:])
            i+=1
        return res

if __name__ == '__main__':
    print Coins().countWays(10)