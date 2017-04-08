BLOCK = 0
EMPTY = 1
HAVERUN = 3 

MAXNUM = 9999999

VERTICLE = 0
HORIZONTAL = 1
UNKNOWN = 2

# N+1 * M+1
# ....bb..
# ........
# .....b..
# ...bb...
#
# paths = [[1,1,1,1,0,0,1,1], [1]*8, [1,1,1,1,1,0,1,1],[1,1,1,0,0,1,1,1]]
#
# dp = [[(MAXNUM, UNKNOWN)]*8,[(MAXNUM,UNKNOWN)]*8,[(MAXNUM,UNKNOWN)]*8,[(MAXNUM,UNKNOWN)]*8]
# dp[0][0] = (0, UNKNOWN)
#
# n = 0
# m = 1
#
# N = 4
# M = 8
#
# left = 0;
# if m == 0:
#     left == MAXNUM
# elif paths[n][m-1] == BLOCK:
#     # dp[n][m] = dp[n][m-1]
#     left = MAXNUM
# elif (n == N-1):
#     left = dp[n][m-1][0]
# elif paths[n+1][m-1] == BLOCK:
#     left = dp[n][m-1][0]
# elif dp[n][m-1][1] == UNKNOWN:
#     left = dp[n][m-1][0]
# elif dp[n][m-1][1] == VERTICLE:
#     left = dp[n][m - 1][0] + 1
# elif dp:
#     left = dp[n][m - 1][0]


def calculateDP(N, M):
    paths = [[1, 1, 1, 1, 0, 0, 1, 1], [1] * 8, [1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 0, 0, 1, 1, 1]]
    # dp = [[(MAXNUM, UNKNOWN)] * M, [(MAXNUM, UNKNOWN)] * M, [(MAXNUM, UNKNOWN)] * M, [(MAXNUM, UNKNOWN)] * M]
    dp = [ [(MAXNUM, UNKNOWN)] * M for _ in range(0, N)]
    dp[0][0] = (0, UNKNOWN)
    for n in range(0, N):
        for m in range(0, M):
            if m == 0 and n == 0:
                continue
            calculateInnterDP(n, m, N, M, dp, paths)
    print paths
    print dp
    return dp


def calculateInnterDP(n, m, N, M, dp, paths):
    if paths[n][m] == BLOCK:
        dp[n][m] == (MAXNUM, UNKNOWN)
        return
    left = 0
    if m == 0:
        left = MAXNUM
    else:
        if n == N-1:
            left = dp[n][m-1][0]
        else:
            # in the middle
            if paths[n][m-1] == BLOCK:
                left = MAXNUM
            else:
                if dp[n][m-1][1] == UNKNOWN or dp[n][m-1][1] == VERTICLE:
                    left = dp[n][m-1][0]
                else:
                    if paths[n+1][m-1] == BLOCK:
                        left = dp[n][m - 1][0]
                    else:
                        left = dp[n][m - 1][0] + 1
    up = 0
    if n == 0:
        up = MAXNUM
    else:
        if m == M - 1:
            up = dp[n - 1][m][0]
        else:
            # in the middle
            if paths[n-1][m] == BLOCK:
                up = MAXNUM
            else:
                if dp[n-1][m][1] == UNKNOWN or dp[n-1][m][1] == HORIZONTAL:
                    up = dp[n - 1][m][0]
                else:
                    if paths[n-1][m+1] == BLOCK:
                        up = dp[n-1][m][0]
                    else:
                        up = dp[n - 1][m][0] + 1
    if left > up:
        dp[n][m] = (up, HORIZONTAL)
    elif left == up:
        dp[n][m] = (up, UNKNOWN)
    else:
        dp[n][m] = (left, VERTICLE)
    return

if __name__ == '__main__':
    dp = calculateDP(4,8)
    print dp[3][7][0]

# ....bb..
# ........
# .....b..
# ...bb...
#
# 1, 1, 1, 1, 0, 0, 1, 1
# 1, 1, 1, 1, 1, 1, 1, 1
# 1, 1, 1, 1, 1, 0, 1, 1
# 1, 1, 1, 0, 0, 1, 1, 1

