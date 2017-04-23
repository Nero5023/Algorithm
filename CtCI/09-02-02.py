# -*- coding:utf-8 -*-
class Robot:
    def countWays(self, m, x, y):
        # write code here
        dp = [[0]*(y+1) for _ in range(0,x+1)]
        if m[0][0] == 0:
            return 0
        for i in range(1,x+1):
            for j in range(1, y+1):
                if i == 1 and j == 1:
                    dp[i][j] = 1
                    continue
                if m[i-1][j-1] == 1:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000007
        return dp[x][y]


if __name__ == '__main__':
    print Robot().countWays([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,0,1,1],[0,1,1,1],[1,1,1,1],[1,1,1,1]],11,4)