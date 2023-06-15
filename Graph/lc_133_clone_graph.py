import collections


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(self, node: 'Node'):
    # check input value
    if not node: return Node
    oldToNew = dict()

    def dfs (node):
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node)

    q = collections.deque([node])
    oldToNew = {}
    copy = Node(node.val)
    oldToNew[node] = copy
    while q:
        cur = q.popleft()
        cur_clone = oldToNew[cur]
        for nei in cur.neighbors:
            if nei not in oldToNew:
                q.append(nei)
                oldToNew[nei] = Node(nei.val)
            cur_clone.neighbors.append(oldToNew[nei])
    return oldToNew[node]
