class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 贪心
        # 记录一个当前范围内的最大值，从前向后遍历，遇到num[i]<nums[i+1]的，就count+=1，否则就重新计count=1
        n = len(nums)
        if n < 2:
            return n
        count = 1
        res = 1
        for i in range(0,n-1):
            if nums[i] < nums[i+1]:
                count += 1
            else:
                count = 1
            res = max(res,count)
        return res  
    
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 动态规划
        # dp[i]以下标i为结尾的连续递增的子序列长度为dp[i]
        # 递推公式，如果nums[i]>nums[i-1]，那么dp[i]=dp[i-1]+1
        # 初始化所有为1
        # 从前向后遍历
        n = len(nums)
        if n < 2:
            return n
        res = 1
        dp = [1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
            res = max(res,dp[i])
        return res 
        