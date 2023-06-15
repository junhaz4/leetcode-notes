import collections


def numIslands(self, grid: list[list[str]]) -> int:
    # check input value
    if not grid:
        return 0
    rows, columns  = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r,c):
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))
        while q:
            row, col = q.popleft()
            direction = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr, dc in direction:
                r, c = row+dr, col+dc
                if r in range(rows) and c in range(columns) and grid[r][c] == "1" and (r,c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == '1' and (r,c) not in visited:
                bfs(r,c)
                islands += 1
    return islands