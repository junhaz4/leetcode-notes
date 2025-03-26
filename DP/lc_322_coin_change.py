class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[j]从coins中取出一些coin组成和为j的的最少个数
        # 凑足总额为j - coins[i]的最少个数为dp[j - coins[i]]，那么只需要加上一个钱币coins[i]，即dp[j - coins[i]] + 1
        # dp[0] = 0，凑足总金额为0所需钱币的个数一定是0
        # 因为求最小值，所以初始化int_max
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(1,amount+1):
                if j >= coin:
                    dp[j] = min(dp[j],dp[j-coin]+1)
        
        return dp[amount] if dp[amount] < float("inf") else -1