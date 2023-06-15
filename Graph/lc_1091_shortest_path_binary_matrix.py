import collections
class Solution:
    def shortestPathBinaryMatrix(self, grid):
        if not grid or grid[0][0] or grid[-1][-1]:
            return -1
        m, n = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [-1, -1], [1, 1], [-1, 1]]
        que = collections.deque([(0, 0, 1)])

        while que:
            r, c, count = que.popleft()
            if (r,c) == (m-1,n-1):
                return count
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if 0<=row<m and 0<=col<n and grid[row][col]==0:
                    grid[row][col]=1
                    que.append((row,col,count+1))
        return -1