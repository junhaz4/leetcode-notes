class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp[i][0] 表示第i天持有股票所得最多现金。 dp[i][1] 表示第i天不持有股票所得最多现金
        # 如果第i天持有股票即dp[i][0]
            # 第i-1天就持有股票 dp[i-1][0]
            # 第一天买入股票，dp[i-1][1]-prices[i]
            # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
        # 如果第i天不持有股票即dp[i][1]的情况
            # 第i-1天就不持有股票 dp[i-1][1]
            # 第i天卖出股票，需要额外手续费dp[i-1][0]+prices[i]-fee
            # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee);
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1,n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i-1][0]+prices[i]-fee)
        return max(dp[n - 1][0], dp[n - 1][1])