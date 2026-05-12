class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        def dfs(r, c):
            if (min(r, c) < 0 or r == ROWS
                or c == COLS or grid[r][c] == 0
                or (r, c) in visited):
                return 0
            visited.add((r, c))
            count = 1
            count += dfs(r - 1, c)
            count += dfs(r + 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)
            return count

        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == 1 and (r, c) not in visited):
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area