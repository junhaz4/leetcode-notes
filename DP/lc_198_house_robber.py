class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i]表示[0,i]以内的房屋最多可以偷窃的金额
        # 递推公式
            # 偷第i个，dp[i]=nums[i]+dp[i-2]因为不能偷相邻的
            # 不偷第i个,dp[i] = dp[i-1]
            # 取最大的
        # 初始化 dp[0] = nums[0],dp[1] = max(nums[1],nums[0]) 
        # 遍历顺序，从前向后
        n = len(nums)
        if n <= 1:
            return nums[0]
        dp = [0]*n 
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 2维DP
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]  # 创建二维动态规划数组，dp[i][0]表示不抢劫第i个房屋的最大金额，dp[i][1]表示抢劫第i个房屋的最大金额
        dp[0][1] = nums[0]  # 抢劫第一个房屋的最大金额为第一个房屋的金额
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])  # 不抢劫第i个房屋，最大金额为前一个房屋抢劫和不抢劫的最大值
            dp[i][1] = dp[i-1][0] + nums[i]  # 抢劫第i个房屋，最大金额为前一个房屋不抢劫的最大金额加上当前房屋的金额

        return max(dp[n-1][0], dp[n-1][1])  # 返回最后一个房屋中可抢劫的最大金额