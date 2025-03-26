class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1.持有股票状态（今天购买或者昨天就持有）
        # 不持有股票
            # 2.之前就不持有股票
            # 3.今天卖出
        # 4.今天为冷冻期
        # 达到买入股票状态（状态一）即：dp[i][0]
            # 前一天就是持有状态 dp[i][0] = dp[i - 1][0]
            # 今天买入了
                # 前一天是冷冻期（状态四），dp[i - 1][3] - prices[i]
                # 前一天是保持卖出股票的状态（状态二），dp[i - 1][1] - prices[i]
        # 达到保持卖出股票状态（状态二）即：dp[i][1]
            # 前一天就是状态二
            # 前一天是冷冻期（状态四）
        # 达到今天就卖出股票状态（状态三），即：dp[i][2]
            # 昨天一定是持有股票状态（状态一），今天卖出
        # 达到冷冻期状态（状态四），即：dp[i][3]，
            # 昨天卖出了股票（状态三）
        # 初始化，如果是持有股票状态（状态一）那么：dp[0][0] = -prices[0]，一定是当天买入股票。
        n = len(prices)
        dp = [[0]*4 for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i]))
            dp[i][1] = max(dp[i-1][1],dp[i-1][3])
            dp[i][2] = dp[i-1][0]+prices[i]
            dp[i][3] = dp[i-1][2]
        return max(dp[n-1][1],dp[n-1][2],dp[n-1][3])
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 上面的状态二和四可以合并成一个
        n = len(prices)
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = -prices[0]  # 持有股票的最大利润
        dp[0][1] = 0           # 不持有股票，且冷冻期的最大利润
        dp[0][2] = 0           # 不持有股票，且能够买的最大利润
        for i in range(1, n):
            # 前一天就持有股票或者前一天不持有但是能购买+今天买入
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            # 前一天持有股票+今天买入
            dp[i][1] = dp[i-1][0] + prices[i]
            # 前一天就不持有股票且没买入或者前一天是冷冻期无法买入
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])

        # 返回最后一天不持有股票的最大利润
        return max(dp[-1][1], dp[-1][2])
