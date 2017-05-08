class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if (i,j) in visited:
                    continue
                else:
                    if grid[i][j] == '1':
                        islands += 1
                        self.visitAround(grid, i, j, visited)
                    else:
                        visited.add((i,j))
        return islands


    def visitAround(self, grid, x, y, visited):
        if not self.validIndex(grid, x, y):
            return
        if (x,y) in visited:
            return
        visited.add((x,y))
        if grid[x][y] == '0':
            return
        self.visitAround(grid, x+1, y, visited)
        self.visitAround(grid, x, y+1, visited)
        self.visitAround(grid, x-1, y, visited)
        self.visitAround(grid, x, y-1, visited)

    def validIndex(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
            return False
        return True

if __name__ == '__main__':
    s = Solution()
    print s.numIslands(["11110","11010","11000","00000"])