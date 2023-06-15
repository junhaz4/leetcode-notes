'''
模拟顺时针画矩阵的过程:
填充上行从左到右
填充右列从上到下
填充下行从右到左
填充左列从下到上
由外向内一圈一圈这么画下去
坚持循环不变量原则
'''
class Solution:
    def generateMatrix(self, n: int):
        # [l,r)
        # time: O(n^2)
        # space O(1) not using extra space
        matrix = [[0] * n for _ in range(n)]
        startx = 0 # represent row
        starty = 0 # represent column
        loop = n//2
        count = 1
        offset = 1
        while loop:
            # fill up the top row from left to right
            for j in range(starty,n-offset):
                matrix[startx][j] = count
                count += 1
            # fill up the right column from top to bottom
            for i in range(startx,n-offset):
                matrix[i][n-offset] = count
                count += 1
            # fill up the bottom row from right to left
            for j in range(n-offset,starty,-1):
                matrix[n-offset][j] = count
                count += 1
            # fill up the left column from bottom to top
            for i in range(n-offset,startx,-1):
                matrix[i][starty] = count
                count += 1
            loop -= 1
            offset += 1
            starty += 1
            startx += 1
        if n % 2 == 1:
            matrix[n//2][n//2] = count
        return matrix

# Method 2
class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        count = 1
        while left < right and up < down:
            # fill up top row from left to right
            for j in range(left, right):
                matrix[up][j] = count
                count += 1
            # fill up right column from top to bottom
            for i in range(up, down):
                matrix[i][right] = count
                count += 1
            # fill up bottom row from right to left
            for j in range(right, left, -1):
                matrix[down][j] = count
                count += 1
            # fill up left column from bottom to top
            for i in range(down, up, -1):
                matrix[i][left] = count
                count += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        if n % 2 == 1:
            matrix[n//2][n//2] = count
        return matrix