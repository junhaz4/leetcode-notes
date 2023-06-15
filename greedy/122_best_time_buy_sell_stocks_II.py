class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 分解利润以每天为单位：假设第0天买入，第i天卖出，每天的利润序列：(prices[i] - prices[i - 1]).....(prices[1] - prices[0])。
        # 只收集正利润
        # time O(n) space O(1)
        res = 0
        for i in range(1,len(prices)):
            res += max(prices[i]-prices[i-1],0)
        return res

# method 2 DP
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # time O(n) space O(n)
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])  # 注意这里是和121. 买卖股票的最佳时机唯一不同的地方
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[-1][1]