class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        par = [i for i in range(n + 1)]
        ranks = [0] * (n + 1)

        def find(x):
            while x != par[x]:
                par[x] = find(par[x])
                x = par[x]
            return x

        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if ranks[rx] > ranks[ry]:
                par[ry] = rx
                ranks[rx] += 1
            else:
                par[rx] = ry
                ranks[ry] += 1
            return True

        for i, j in edges:
            if not union(i,j):
                return[i,j]
        return True
