# advanced level of lc 200-number of islands
import collections
class Solution:
    def maxAreaOfIsland(self, grid):
        ### method 1
        if not grid:
            return 0
        visited = set()
        max_area = 0
        m, n = len(grid), len(grid[0])

        def bfs(r, c):
            que = collections.deque()
            visited.add((r, c))
            que.append((r, c))
            area = 1
            while que:
                row, col = que.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(m) and c in range(n) and grid[r][c] == 1 and (r, c) not in visited:
                        area += 1
                        que.append((r, c))
                        visited.add((r, c))
            return area

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    max_area = max(max_area, bfs(i, j))

        #return max_area

    ### method 2
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if (r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        area = 0
        for i in range(rows):
            for j in range(cols):
                area = max(area,dfs(i,j))
        #return area

    ### method 3 optimized dfs
        rows, cols = len(grid), len(grid[0])
        def dfs(r,c):
            if (0<=r<rows and 0<=c<cols and grid[r][c]==1):
                grid[r][c] = 0
                return (1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]==1]
        return max(areas) if areas else 0

