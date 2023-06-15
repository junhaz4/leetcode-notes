def orangesRotting(grid):
    '''
    The idea is to use bfs level order traversal to contaminate organge in each level
    First loop through the grid the find the number of fresh and the initial rotten
    Initialize the time and set the contamination direction in all four directions
    For each rotten in queue, contaminate the neighbors in four directions
    Put the newly rotten into queue, decrement the fresh 
    After current rotten done, if there is rotten in queue, increment the time
    return time if fresh is 0 and -1 otherwise
    '''
    from collections import deque
    queue= deque()
    rows = len(grid)
    columns = len(grid[0])
    fresh = 0
    for r in range(rows):
        for c in range(columns):
            if grid[r][c]==2:
                queue.append([r,c])
            elif grid[r][c]==1:
                fresh+=1
    minutes = 0
    direction = [(0,1),(1,0),(-1,0),(0,-1)]
    while queue:
        size = len(queue)
        for _ in range(size):
            row,column = queue.popleft()
            for d in direction:
                neighbor_row, neighbor_column = row+d[0], column+d[1]
                if (0<=neighbor_row<rows) and (0<=neighbor_column<columns):
                    if grid[neighbor_row][neighbor_column] == 1:
                        grid[neighbor_row][neighbor_column]=2
                        fresh -=1
                        queue.append([neighbor_row, neighbor_column])
        if queue:
            minutes+=1
            
    if fresh ==0:
        return minutes 
    else:
        return -1
'''
grid = 
[[2,1,1],[1,1,0],[0,1,1]]
[[2,1,1],[1,1,0],[0,1,1]]
[[0,2]]
[[0,1],[1,0]]
[[0,1],[2,0]]
[[2,1,1],[1,1,0],[0,1,2]]
[[2,2],[1,1],[0,0],[2,0]]
[[2,2],[1,1],[0,0],[2,0]]
'''
