import collections

class Solution:
    def longestIncreasingPath(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        # hashmap (r,c) => LIP
        dp = {}

        def dfs(r, c, prev):
            if (r < 0 or r == rows or
                    c < 0 or c == cols or
                    matrix[r][c] <= prev):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            up = dfs(r + 1, c, matrix[r][c])
            down = dfs(r - 1, c, matrix[r][c])
            right = dfs(r, c + 1, matrix[r][c])
            left = dfs(r, c - 1, matrix[r][c])
            path = 1 + max(up, down, right, left)
            dp[(r, c)] = path
            return path

        for row in range(rows):
            for col in range(cols):
                # initialize previous cell value use -1 since the smallest cell value is 0
                dfs(row, col, -1)
        return max(dp.values())


### Method 2 Topological Sort By Kahn's algorithm(BFS)
    def longestIncreasingPath(self, matrix):
        '''
        Convert to matrix into a graph:
        1. Each cell is a node
        2. a directed edge from x to y if xm y are adjacent and x'value < y'value
        No cycles in the graph, so it's a DAG
        The problem becomes to get the longest path in the DAG.
        Topological sort can iterate the vertices of a DAG in the linear ordering.
        Using Kahn's algorithm(BFS) to implement topological sort
        while counting the levels can give us the longest chain of nodes in the DAG.
        '''
        rows, cols = len(matrix), len(matrix[0])
        indegree = [[0 for x in range(cols)] for y in range(rows)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]

        # get indegree of the graph
        for row in range(rows):
            for col in range(cols):
                for dr,dc in directions:
                    nr, nc = row+dr, col+dc
                    if nr in range(rows) and nc in range(cols):
                        if matrix[nr][nc] < matrix[row][col]:
                            indegree[row][col] += 1

        # get queue
        queue= collections.deque()
        for row in range(rows):
            for col in range(cols):
                # indegree 0 => no dependencies
                if indegree[row][col] == 0:
                    queue.append((row,col))

        # get the longest path
        path_len = 0
        while queue:
            path_len += 1
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols):
                        # update indegree after removing zero dependency nodes from the graph
                        if matrix[nr][nc] > matrix[r][c]:
                            indegree[nr][nc] -= 1
                            if indegree[nr][nc] == 0:
                                queue.append((nr,nc))
        return path_len

