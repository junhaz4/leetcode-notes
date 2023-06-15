class Solution:
    def findSubsequences(self, nums: list[int]):
        # method 1
        self.result = []
        self.path = []
        def backtracking(nums,startIndex):
            if len(self.path)>=2:
                self.result.append(self.path[:])
            if startIndex >= len(nums):
                return
            used = set()
            for i in range(startIndex,len(nums)):
                # if the current element is less than the previous one or the current is already used, continue for the next loop
                if (self.path and nums[i]<self.path[-1]) or nums[i] in used:
                    continue
                used.add(nums[i])
                self.path.append(nums[i])
                backtracking(nums,i+1)
                self.pop()
                # Similar method but in the opposite direciton
                '''
                if (not path or nums[i]>=path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    path.append(nums[i])
                    backtracking(nums,i+1)
                    path.pop()
                else:
                    continue
                '''
        backtracking(nums,0)
        return self.result 
    
        # Method 2 use hashtable to check repetiion
        self.result = []
        self.path =[]
        def backtrack(nums,startIndex):
            if len(self.path)>=2:
                self.result.append(self.path[:])
            if startIndex >= len(nums):
                return
            used = [False]*201
            for i in range(startIndex,len(nums)):
                if (self.path and nums[i]<self.path[-1]) or used[nums[i]+100]==True:
                    continue
                used[nums[i]+100]=True
                self.path.append(nums[i])
                backtracking(nums,i+1)
                self.pop()
        backtrack(nums,0)
        return self.result