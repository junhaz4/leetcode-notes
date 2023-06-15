class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        '''
        To find all subsets, need to store all subsets in the node both leaf node and unleaf node
        '''
        self.result = []
        self.path = []
        def backtracking(nums,startIndex):
            # collect subsets
            self.result.append(self.path)
            for i in range(startIndex,len(nums)):
                self.path.append(nums[i])
                backtracking(nums,i+1)
                self.path.pop()
        backtracking(nums,0)
        return self.result