from audioop import reverse
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(row,col,val,board):
            # check row 
            for i in range(9):
                if board[row][i]==str(val):
                    return False
            # check column
            for j in range(9):
                if board[j][col]==str(val):
                    return False
            # check 3x3 boxes
            startrow = (row//3)*3
            startcol = (col//3)*3
            for i in range(startrow, startrow+3):
                for j in range(startcol, startcol+3):
                    if board[i][j]==str(val):
                        return False 
            return True
        
        def backtracking(board):
            # traversal each row
            for i in range(9):
                # traveral each column
                for j in range(9):
                    # if the cell is not empty,move to next
                    if board[i][j] !='.':
                        continue
                    # check which number is valid to put in (i,j)
                    for k in range(1,10):
                        if is_valid(i,j,k,board):
                            board[i][j]=str(k)
                            # if found a solution, return 
                            if backtracking(board):
                                return True
                            board[i][j]='.'
                    return False  # if none of the nine numbers work, means no solution, return False 
            return True # no False after traversal, means there exists a solution, return True
        backtracking(board)