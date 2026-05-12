class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        self.dfs(image, sr, sc, original_color, color, set())
        return image
    def dfs(self, image, r, c, original_color, color, visited):
        ROWS, COLS = len(image), len(image[0])
        if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited
            or image[r][c] != original_color):
            return
        
        visited.add((r, c))
        
        image[r][c] = color

        self.dfs(image, r + 1, c, original_color, color, visited)
        self.dfs(image, r - 1, c, original_color, color, visited)
        self.dfs(image, r, c + 1, original_color, color, visited)
        self.dfs(image, r, c - 1, original_color, color, visited)
        
        visited.remove((r, c))