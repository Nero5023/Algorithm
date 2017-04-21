class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        if amount == 0:
            return 0
        res = self.coinChangeIter(coins, amount)
        if res == 0:
            return -1
        return res
        
    def coinChangeIter(self, coins, money):
        if money < 0:
            return 0;
        if money == 0:
            return 1
        if len(coins) == 0:
            return 0
        if coins[0] == 1:
            return 1
        i = 0
        res = 0
        while money - i*coins[0] >= 0:
            res += self.coinChangeIter(coins[1:], money - i*coins[0])
            i+=1
        return res

if __name__ == '__main__':
    print Solution().coinChange([2], 0)