def search_2D(matrix, target):
    m, n = len(matrix), len(matrix[0])
    if m == 0:
        return False
    left, right = 0, m*n
    while left <- right:
        mid = left + (right-left)//2
        number = matrix[mid//n][mid%n]
        if number == target:
            return True
        elif number < target:
            left = mid+1
        else:
            right = mid-1
    return False

# time complexity: O(logn + logm)
# space: O(1)