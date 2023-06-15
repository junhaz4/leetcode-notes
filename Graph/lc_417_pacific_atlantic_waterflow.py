import collections

class Solution:
    def pacificAtlantic(self, heights):
        '''
        Approach this problem from the opposite direction. Instead of finding which cell can flow water to pacific and atlantic,
        we find that if we start from the boundary cells/if we start from the ocean, what are some cells can water flow to,
        which is the value of current cell is small or equal to the neighbor cells.
        '''
        ### Method 1 - DFS
        if not heights: return []
        rows, cols = len(heights), len(heights[0])
        a_visited, p_visited = set(), set()

        def dfs(r,c,visited):
            # if the cell is already visited, skip it
            if (r,c) in visited:
                return
            visited.add((r,c))
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr, dc in direction:
                new_r, new_c = r+dr, c+dc
                if (new_r,new_c) not in visited and new_r in range(rows) and new_c in range(cols):
                    # check if water can flow to the neighbor cell
                    if heights[new_r][new_c] >= heights[r][c]:
                        dfs(new_r,new_c,visited)

        # start from first column
        for row in range(rows):
            dfs(row,0,p_visited)
            dfs(row,cols-1,a_visited)

        # start from the first row
        for col in range(cols):
            dfs(0, col, p_visited)
            dfs(rows - 1, col, a_visited)

        #return list(a_visited&p_visited)

        ### Method 2 - BFS
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        p_que = collections.deque()
        a_que = collections.deque()

        def bfs(q, visited):
            directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
            while q:
                i, j = q.popleft()
                if (i, j) in visited:
                    continue
                visited.add((i, j))

                for direction in directions:
                    x, y = i + direction[0], j + direction[1]
                    if 0 <= x < rows and 0 <= y < cols and heights[x][y] >= heights[i][j]:
                        q.append((x, y))

        for i in range(rows):
            a_que.append((i, cols - 1))
            p_que.append((i, 0))

        for j in range(cols):
            a_que.append((rows - 1, j))
            p_que.append((0, j))

        bfs(a_que, a_visited)
        bfs(p_que, p_visited)


        return list(a_visited & p_visited)
