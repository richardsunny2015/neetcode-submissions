class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numOfRows = len(matrix)
        numOfCols = len(matrix[0])
        l = 0
        r = (numOfRows * numOfCols) - 1

        while l <= r:
            m = (l + r) // 2
            row = m // numOfCols
            col = m % numOfCols
            n = matrix[row][col]
            if n < target:
                l = m + 1
            elif n > target:
                r = m - 1
            else:
                return True
        return False
                