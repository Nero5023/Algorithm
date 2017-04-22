class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        n = len(board[0])
        res = 0
        for row in range(0, m):
            for col in range(0, n):
                if board[row][col] == "X" and (col == 0 or board[row][col-1] == ".") and (row == 0 or board[row-1][col] == "."):
                    res += 1
        return res