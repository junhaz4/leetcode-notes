class Solution:
    def permute(self, nums: list[int]):
        '''
        Different from the combination problem, search starts from index 0 not startIndex in each level and self.used is used to check repetition.
        '''
        self.result = []
        self.path = []
        self.used = [False]*len(nums)
        def backtracking(nums,used):
            if len(self.path)==len(nums):
                self.result.append(self.path[:])
                return
            for i in range(len(nums)):
                # no extra space used 
                # if nums[i[ in self.path:
                if self.used[i]==True:
                    continue
                used[i]=True
                self.path.append(nums[i])
                backtracking(nums,used)
                used[i]=False
                self.path.pop()
        backtracking(nums,self.used)
        return self.result 