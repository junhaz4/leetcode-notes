class Solution:
    def permuteUnique(self, nums: list[int]):
        result = []
        path = []
        used = [False]*len(nums)
        nums.sort()
        def backtracking(nums,used):
            if len(path)==len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                # check repetition
                if used[i]==False:
                    if i>0 and nums[i]==nums[i-1] and used[i-1]==False:
                        continue
                    path.append(nums[i])
                    used[i] = True
                    backtracking(nums,used)
                    used[i] = False
                    path.pop()
        backtracking(nums,used)
        return result 