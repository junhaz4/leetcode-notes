import collections
class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        The idea is that we start the BFS from the gates.
        Each gate is not fully searched before moving to the next gate only look at areas within 1 space before the next gate.
        So each area within one space of the gated is checked and marked and then put into the queue as the new gate
        once a gate reached an empty room and marks it with the distance, that room must be closest to that gate
        (compared to the rest of the gates) because that gate is the 1st gate to reach that room.
        """
        if not rooms:
            return rooms
        rows, cols = len(rooms), len(rooms[0])
        queue = collections.deque()

        # get all gates and convert all walls to -1
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append([r, c])

        # traversal one gate at a time to areas within one space at the same time
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr == rows or
                        nc < 0 or nc == cols or
                        rooms[nr][nc] != 2147483647):
                    continue
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append([nr, nc])

# Method 2 traversa all gates at the same to areas within 1 space.
def wallsAndGates(self, rooms) -> None:
    rows, cols = len(rooms), len(rooms[0])
    queue = collections.deque()
    visited = set()

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append([r, c])
                visited.add((r,c))

    def bfs(r,c):
        if (r < 0 or r == rows or
            c < 0 or c == rows or
            (r,c) in visited or rooms[r][c] == -1):
            return
        visited.add((r,c))
        queue.append([r,c])

    dist = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            rooms[r][c] = dist
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)
        dist += 1
