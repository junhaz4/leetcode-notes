class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []
        def backtracking(n,k,start):
            if len(path)==k:
                result.append(path)
                return 
            for i in range(start,n+1):
           # for i in range(start,n+2-(k-len(path))): 
           # reduce extra steps if the remaining element isn't enough to form a path of size k
           # eg n=4,k=3, then only need to consider backtracking on 1 and 2 since 3 and 4 not form a path of size 3
                path.append(i)
                backtracking(n, k, i+1)
                path.pop()
        backtracking(n, k, 1)
        return result
    
    
