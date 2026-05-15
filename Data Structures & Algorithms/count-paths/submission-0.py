class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0] * n] * m
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    paths[row][col] = 1
                else:
                    paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
        return paths[m - 1][n - 1]


# 0 1 1 1 1 1
# 1 2 3
# 1 3 