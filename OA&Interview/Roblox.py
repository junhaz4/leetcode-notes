def drop_game(board):
    if not board:
        return 0
    row, col = len(board), len(board[0])
    obstacle = []
    # find all obstacles
    for r in range(row):
        for c in range(col):
            if board[r][c] == "#":
                obstacle.append([r,c])
    bottom_r, bottom_c = 0, 0
    for r in range(row-1,-1,-1):
        for c in range(col-1,-1,-1):
            if board[r][c] == '*':
                bottom_r, bottom_c = r, c
                break
    distance = row-bottom_r-1
    count = 0
    for r,c in obstacle:
        for i in range(1,distance+1):
            if 0<= r-i < row and board[r-i][c] == "#":
                count += 1
                break
    return count

def solution(row,col,black):
    seen = set()
    res = [0]*5
    for r,c in black:
        # top let
        count = 0
        if [[r,c],[r+1,c],[r,c+1],[r+1,c+1]] not in seen:
            continue
        else:
            if 0 <= r+1 < row and [r+1,c] in black:
                count += 1
            if  0<= c+1 < col and [r,c+1] in black:
                count += 1
            if 0 <= r+1 < row and 0<= c+1 < col and [r+1,c+1] in black:
                count += 1
            res[count] += 1
            seen.add([[r,c],[r+1,c],[r,c+1],[r+1,c+1]])
        # top right
        if [[r, c], [r + 1, c], [r, c - 1], [r + 1, c -1]] in seen:
            continue
        else:
            count = 0
            if 0 <= r + 1 < row and [r + 1, c] in black:
                count += 1
            if 0 <= c - 1 < col and [r, c - 1] in black:
                count += 1
            if 0 <= r + 1 < row and 0 <= c - 1 < col and [r + 1, c - 1] in black:
                count += 1
            res[count] += 1
            seen.add([[r, c], [r + 1, c], [r, c - 1], [r + 1, c -1]])
        # bottom left
        if [[r, c], [r - 1, c], [r, c + 1], [r - 1, c + 1]] in seen:
            continue
        else:
            count = 0
            if 0 <= r - 1 < row and [r - 1, c] in black:
                count += 1
            if 0 <= c + 1 < col and [r, c + 1] in black:
                count += 1
            if 0 <= r - 1 < row and 0 <= c + 1 < col and [r - 1, c + 1] in black:
                count += 1
            res[count] += 1
            seen.add([[r, c], [r - 1, c], [r, c + 1], [r - 1, c + 1]])
        # bottom right
        if [[r, c], [r -1, c], [r, c - 1], [r - 1, c - 1]] in seen:
            continue
        else:
            count = 0
            if 0 <= r - 1 < row and [r - 1, c] in black:
                count += 1
            if 0 <= c - 1 < col and [r, c - 1] in black:
                count += 1
            if 0 <= r - 1 < row and 0 <= c - 1 < col and [r - 1, c - 1] in black:
                count += 1
            res[count] += 1
            seen.add([[r, c], [r -1, c], [r, c - 1], [r - 1, c - 1]])
    return res