import collections

class Solution:
    def orangesRotting(self, grid) -> int:
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        minutes, fresh = 0, 0
        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue and fresh > 0:
            size = len(queue)
            for _ in range(size):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        fresh -= 1
                        grid[nr][nc] = 2
            minutes += 1
        return minutes if fresh==0 else -1