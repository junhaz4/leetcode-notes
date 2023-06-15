"""
Disjoint set and Union Find

Find(x): find the root of x  O(1)
Union(x,y): merge two elements in the same set O(1)
space: O(n)

Optimizations:
1. path compression: make tree flat happened during Find
2. union by rank: merge low rank tree to high rank tree
"""

class unionfind:
    def __init__(self,n):
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for i in range(n + 1)]

    def find(self, u):
        """
        if self._parents[u] == u:
            return u
        self._parents[u] = self.find(self._parents[u])
        return self._parents[u]
        """
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
            self._ranks[pv] += 1
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        '''
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        '''
        return True