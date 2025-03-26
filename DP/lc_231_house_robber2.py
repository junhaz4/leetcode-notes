class Solution:
    def rob(self, nums: List[int]) -> int:
        # 因为成环，需要注意头和尾部不能同时偷，所以可以从头走一遍不包含尾部，从第二个走一遍不包含头部，取最大
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        res1 = self.rob_range(nums[:-1])
        res2 = self.rob_range(nums[1:])
        return max(res1,res2)

    def rob_range(self,nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0]*n 
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]