class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        n = len(nums)
        dp = [0]*n  # dp[i]表示包括i之前的最大连续子序列和
        dp[0] = nums[0]
        result = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            result = max(result,dp[i])  # result记录dp[i]的最大值
        return result 