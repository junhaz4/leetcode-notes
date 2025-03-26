class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Best Time to Buy and Sell Stock III
        # 使用同样的dp定义dp[i][j]，可以发现奇数就是卖出，偶数就是买入，所以j的范围就是2k+1
        n = len(prices)
        dp = [[0]*(2*k+1) for _ in range(n)]
        for j in range(1,2*k,2):
            dp[0][j] = -prices[0]
        for i in range(1,n):
            for j in range(0,2*k-1,2):
                dp[i][j+1] = max(dp[i-1][j+1],dp[i-1][j]-prices[i])
                dp[i][j+2] = max(dp[i-1][j+2],dp[i-1][j+1]+prices[i])
        return dp[-1][-1]