class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        # return self.search2DMatrix(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, target)
        return self.fastSearch(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, target)
    
    def search2DMatrix(self, matrix, x0, x1, y0, y1, target):
        if x0 == x1 and y0 == y1:
            return matrix[x0][y0] == target
        if x0 > x1 or y0 > y1:
            return False
        midX = int((x0+x1)/2)
        midY = int((y0+y1)/2)
        if matrix[midX][midY] == target:
            return True
        if matrix[midX][midY] < target:
            return self.search2DMatrix(matrix, midX+1, x1, midY+1, y1, target) \
                or self.search2DMatrix(matrix, midX+1, x1, y0, midY, target) \
                or self.search2DMatrix(matrix, x0, midX, midY+1, y1, target)
        else:
            return self.search2DMatrix(matrix, x0, midX-1, y0, midY-1, target) \
                or self.search2DMatrix(matrix, x0, midX-1, midY, y1, target) \
                or self.search2DMatrix(matrix, midX, x1, y0, midY-1, target)

    def fastSearch(self, matrix, x0, x1, y0, y1, target):
        if x0 == x1 and y0 == y1:
            return matrix[x0][y0] == target
        if x0 > x1 or y0 > y1:
            return False
        topRight = matrix[x0][y1]
        if topRight == target:
            return True
        if topRight > target:
            return self.fastSearch(matrix, x0, x1, y0, y1-1, target)
        if topRight < target:
            return self.fastSearch(matrix, x0+1, x1, y0, y1, target)

if __name__ == '__main__':
    so = Solution()
    print(so.searchMatrix([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]], 15))
    print(so.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], ))