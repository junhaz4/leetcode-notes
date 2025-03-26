class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 从coins中选择一些，组成和为amount的方案数，由于每种coin可以无限次选择，所以是完全背包
        # 定义：dp[i][j]使用下标为[0,i]的coins[i]能够凑满j（包括j）容量的包，有dp[i][j]种组合方法
        # 递推公式
            # 不选i，从[0,i-1]中选择，dp[i-1][j]
            # 选i，先把i的容量流出来，因为i可以重复选，所以选完i后可以接着从[0,i]中选dp[i][j-coins[i]]
            # 求方案数，所以对这两种情况求和
        # 初始化，i=0和j=0的情况需要处理
        # 从前往后遍历，先遍历coins，再遍历容量
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        # 初始化首行 i=0, 用物品0装满背包容量为j的背包,只有j能整除物品0，那么就有1种方法
        for j in range(coins[0],amount+1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        # 初始化首列 j=0, 用物品i装满容量为0的背包有且只有1种方法
        for i in range(n):
            dp[i][0] = 1 

        for i in range(1,n):
            for j in range(amount+1):
                if coins[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        
        return dp[n-1][amount]

        # 1维DP
        dp = [0]*(amount+1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] = dp[j]+dp[j-coin]
        return dp[amount]