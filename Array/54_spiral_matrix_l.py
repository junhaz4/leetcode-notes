class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # time: O(m*n)
        # space: O(1) not considering the ouput array as we are not using any extra space
        height = len(matrix)
        width = len(matrix[0])
        top, left = 0, 0
        bottom, right = height - 1, width - 1
        result = []
        while left < right and top < bottom:
            # traversal top row from left to right
            for j in range(left, right):
                result.append(matrix[top][j])

            # traversal right column from top to bottom
            for i in range(top, bottom):
                result.append(matrix[i][right])

            # traversal bottom row from right to left
            for j in range(right,left,-1):
                result.append(matrix[bottom][j])

            # traveral left column from bottom to top
            for i in range(bottom, top, -1):
                result.append(matrix[i][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        # If a matrix remain inside it is either a 1xn or a mx1
        # a linear scan will return the same order as spiral for these
        if len(result) < height*width:
            for i in range(top,bottom+1):
                for j in range(left,right+1):
                    result.append(matrix[i][j])
        return result
