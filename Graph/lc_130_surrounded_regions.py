class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def dfs(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or board[r][c] != 'O'):
                return
            board[r][c] = 'T'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)

        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)

        v = {'X':'X',"T":'O',"O":"X"}
        for r in range(rows):
            for c in range(cols):
                board[r][c] = v[board[r][c]]