class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        queue.append((0, 0))
        visit.add((0, 0))

        neighbors = [[-1, -1], [-1, 0], [-1, 1],
                     [0, -1], [0, 1],
                     [1, -1], [1, 0], [1, 1]]
        length = 1
        
        while(len(queue)):
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r == ROWS - 1 and c == COLS - 1):
                    return length

                for dr, dc in neighbors:
                    ar, ac = dr + r, c + dc
                    if (min(ar, ac) < 0 or ar >= ROWS or ac >= COLS
                        or grid[ar][ac] == 1 or (ar, ac) in visit):
                        continue
                    queue.append((ar, ac))
                    visit.add((ar, ac))

            length += 1

        return -1