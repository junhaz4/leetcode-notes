# https://www.techiedelight.com/largest-square-sub-matrix-surrounded-by-1s/
def findLargestSquareSubMatrix(mat):
    if not mat or not len(mat):
        return
    (M, N) = (len(mat), len(mat[0]))
    X = [[0 for x in range(N)] for y in range(M)]
    Y = [[0 for x in range(N)] for y in range(M)]
    for i in range(M):
        for j in range(N):
            if mat[i][j] == "B":
                Y[i][j] = (0 if i == 0 else Y[i - 1][j]) + 1
                X[i][j] = (0 if j == 0 else X[i][j - 1]) + 1
    max_len = 0
    row, col = 0, 0
    for i in reversed(range(M)):
        for j in reversed(range(N)):
            length = min(X[i][j], Y[i][j])
            while length:
                isSquare = Y[i][j - length + 1] >= length and \
                        X[i - length + 1][j] >= length
                if isSquare and max_len < length:
                    max_len = length
                    row, col = i-length+1, j-length+1
                length = length - 1
    return max_len, row, col
 
 
if __name__ == '__main__':
 
    mat = [
        [1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0, 1],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]
    ]
    mat = [
      ["W","W","W"],
      ["W","B","W"],
      ["W","W","W"]
    ]
 
   #print("The size of largest square submatrix is", findLargestSquareSubMatrix(mat))

print('hello')