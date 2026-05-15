class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[0] * n] * m

        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    paths[row][col] = 0
                elif row == 0 or col == 0:
                    if col > 0:
                        paths[row][col] = min(paths[row][col - 1], 1)
                    elif row > 0:
                        paths[row][col] = min(paths[row - 1][col], 1)
                    else:
                        paths[row][col] = 1
                else:
                    paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
        return paths[m - 1][n - 1]
