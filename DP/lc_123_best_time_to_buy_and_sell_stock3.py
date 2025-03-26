class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 每天可以有5中状态
        # 0.无操作
        # 1.第一次持有
        # 2.第一次不持有
        # 3.第二次持有
        # 4.第二次不持有
        # dp[i][j],j=[0,4]第i天在j状态下的现金
        # 递推公式
            # dp[i][0] = dp[i-1][0]
            # dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            # dp[i][2] = max(dp[i-1][2],dp[i-1][1]+prices[i])
            # dp[i][3] = max(dp[i-1][3],dp[i-1][2]-prices[i])
            # dp[i][4] = max(dp[i-1][4],dp[i-1][3]+prices[i])
        # 初始化 
            # dp[0][0] = 0
            # dp[0][1] = -prices[0]
            # dp[0][2] = -prices[0]+prices[0]= 0 当天买入，当天卖出
            # dp[0][3] = dp[0][2]-prices[0]=-prices[0] 第二次买入依赖第一次卖出的状态，第一次卖出后第二次才能买入
            # dp[0][4] = -prices[0]+prices[0]= 0 
        # 遍历顺序，从前向后
        n = len(prices)
        dp = [[0,0,0,0,0] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        for i in range(1,n):
            dp[i][0]=dp[i-1][0]
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
        return dp[n-1][4]