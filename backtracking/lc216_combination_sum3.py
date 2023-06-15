class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        if k > n:
            return []
        result = []
        path = []
        self.sum = 0
        def backtracking(k,n,startIndex):
            # if current sum is greater than n, no need to keep going 
            if self.sum > n:
                return 
            if len(path)==k:
                if self.sum == n:
                    result.append(path[:])
                    return
            for i in range(startIndex,10):
                self.sum += i
                path.append(i)
                backtracking(k,n,i+1)
                path.pop()
                self.sum -= i
        backtracking(k,n,1)
        return result 
