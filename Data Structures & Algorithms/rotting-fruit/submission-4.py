class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0
        queue = deque()
        visit = set()

        neighbors = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def bfs():
            minutes = 0
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in neighbors:
                        ar, ac = dr + r, dc + c
                        if (min(ar, ac) < 0 or ar == ROWS
                            or ac == COLS or (ar, ac) in visit
                            or grid[ar][ac] != 1):
                            continue
                        grid[ar][ac] = 2
                        queue.append((ar, ac))
                        visit.add((ar, ac))
                minutes += 1
            return minutes - 1 if minutes > 0 else 0
        
        def is_all_rotten():
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 1:
                        return False
            return True

        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) not in visit and grid[r][c] == 2):
                    queue.append((r, c))
                    visit.add((r, c))
        minutes = bfs()
        
        if is_all_rotten():
            return minutes
        return -1