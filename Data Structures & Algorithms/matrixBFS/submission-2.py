class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 0

        while(len(queue)):
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [[0, 1], [0, -1], [-1, 0], [1, 0]]

                for dr, dc in neighbors:
                    ar, ac = dr + r, c + dc
                    if (min(ar, ac) < 0 or ar == ROWS or ac == COLS
                        or (ar, ac) in visit or grid[ar][ac] == 1):
                        continue
                    queue.append((ar, ac))
                    visit.add((ar, ac))
            length += 1
        return -1