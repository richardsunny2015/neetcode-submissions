class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    self.dfs(grid, r, c, visited)
        return count
    def dfs(self, grid, r, c, visited):
        ROWS, COLS = len(grid), len(grid[0])
        if (r == ROWS or c == COLS or min(r, c) < 0 or
            grid[r][c] == "0" or (r, c) in visited):
            return
        visited.add((r, c))
        self.dfs(grid, r + 1, c, visited)
        self.dfs(grid, r - 1, c, visited)
        self.dfs(grid, r, c + 1, visited)
        self.dfs(grid, r, c - 1, visited)