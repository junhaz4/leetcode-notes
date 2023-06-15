class Solution:
    def validTree(self, n: int, edges) -> bool:
        # method 1 union find
        if not n:
            return True
        parents = [i for i in range(n)]
        ranks = [0] * n

        def find(x):
            while x != parents[x]:
                parents[x] = find(parents[x])
                x = parents[x]
            return x

        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if ranks[rx] > ranks[ry]:
                parents[ry] = rx
                ranks[rx] += 1
            else:
                parents[rx] = ry
                ranks[ry] += 1
            return True

        for i, j in edges:
            if not union(i,j):
                return False

        res = set()
        for i in range(n):
            res.add(find(i))
        if len(res) == 1:
            return True
        else:
            return False

# method 2 DFS
def validTree(n: int, edges) -> bool:
    if not n: return True
    nodes = {i: [] for i in range(n)}
    visited = set()
    for i, j in edges:
        nodes[i].append(j)
        nodes[j].append(i)

    def dfs(i,prev):
        if i in visited:
            return False
        visited.add(i)
        for j in nodes[i]:
            if j == prev:
                continue
            if not dfs(j,i):
                return False
        return True
    return dfs(0,-1) and len(visited)==n
