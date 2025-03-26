class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        # dp[i][0]表示第i天持有股票的最大现金
        # dp[i][1]表示第i天不持有股票的最大现金
        # 持有不代表当天买入，也可以是之前买入今天仍然持有
        # 递推公式
            # 第i天持有，第i-1天就持有股票或者第i天买入, max(dp[i-1][0],dp[i-1][1]-prices[i])
            # 注意差别，因为可以买卖多次，所以第i天买入的时候第i-1天一定不持有股票，所以使用之前剩下的钱减去股票价格
            # 第i天不持有, 第i-1天不持有或者第i天卖出, max(dp[i-1][1],prices[i]+dp[i-1][0])
        # 初始化dp[0][0] = -prices[0], dp[0][1] == 0
        # 遍历顺序，从前向后遍历
        n = len(prices)
        dp = [[0,0] for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1] = max(dp[i-1][1],prices[i]+dp[i-1][0])
        return dp[-1][1]