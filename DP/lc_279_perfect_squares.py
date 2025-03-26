class Solution:
    def numSquares(self, n: int) -> int:
        # 从小于n的数字中选出平方数，使得这些数字的和为n，平方数就是物品，n就是背包容量
        nums = [i**2 for i in range(1, n + 1) if i**2 <= n]
        dp = [10**4]*(n + 1)
        dp[0] = 0
        # 遍历背包
        for j in range(1, n + 1):
            # 遍历物品
            for num in nums:
                if j >= num:
                    dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]

