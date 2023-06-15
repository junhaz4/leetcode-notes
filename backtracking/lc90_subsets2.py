class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        '''
        use extra array to check if same elements are used more than once
        '''
        self.result = []
        self.path = []
        nums.sort()
        return self.result 
        
        self.used = [False]*len(nums)
        def backtracking(nums,startIndex):
            self.result.append(self.path[:])
            for i in range(startIndex,len(nums)):
                if i>0 and nums[i]==nums[i-1] and self.used[i-1]==False:
                    continue
                self.path.append(nums[i])
                self.used[i]=True
                backtracking(nums,i+1)
                self.used[i]=False
                self.path.pop()
        backtracking(nums,0)
    
        def backtrack(nums,startIndex):
            self.result.append(self.path[:])
            for i in range(startIndex,len(nums)):
                if i>startIndex and nums[i]==nums[i-1]:
                    continue
                self.path.append(nums[i])
                backtrack(nums,i+1)
                self.path.pop()
        backtrack(nums,0)