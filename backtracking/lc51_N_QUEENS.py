class Solution:
    def solveNQueens(self, n: int):
        result = []
        board = [["."]*n for _ in range(n)]
        
        # check not in the same row, not in same column, not in same diagonal line
        def is_valid(row,col,board):
            # 没有在同行进行检查因为在单层搜索的过程中，每一层递归，只会选for循环（也就是同一行）里的一个元素，所以不用去重了。
            # 判断同一列是否冲突
            for i in range(len(board)):
                if board[i][col] == "Q":
                    return False
            # 判断左上角是否冲突
            i = row-1
            j = col-1
            while i>=0 and j>=0:
                if board[i][j]=="Q":
                    return False
                i -= 1
                j -= 1
            # 判断右上角是否冲突
            i = row-1
            j = col+1
            while i>=0 and j< len(board):
                if board[i][j]=="Q":
                    return False
                i -= 1
                j += 1
            return True
        
        def backtracking(n,row,board):
            # 如果走到最后一行，说明已经找到一个解
            if row == n:
                temp = []
                for i in board:
                    s = ''.join(i)
                    temp.append(s)
                result.append(temp)
            for col in range(n):
                if not is_valid(row,col,board):
                    continue
                board[row][col]="Q"
                backtracking(n,row+1,board)
                board[row][col]="."
        backtracking(n,0,board)
        return result 