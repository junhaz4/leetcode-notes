class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 将石头分成两部分，使得其中一部分的重量接近sums/2，那么另一部分的重量也接近sums/2
        # 01背包问题，从stones中选出一些物品放进背包，使得背包的价值接近sums/2
        # dp[i][j] 从[0,i]中选择石头，这些石头的和是否为j
        # 递推公式 dp[i][j] = dp[i-i][j] or dp[i-1][j-stons[i]]
            # 不选i，从[0,i-1]中选择石头组成j
            # 选i，留出i的容量，从[0,i-1]中选择组成j-stones[i]
        # 初始化i和j为0的情况
        # 从前向后遍历
        sums = sum(stones)
        target = sums//2 
        n = len(stones)
        if n <= 1:
            return stones[0]
        dp = [[False]*(target+1) for _ in range(n)]
        for i in range(n): # 初始化第一列，表示总重量为0时，前i个石头都能组成
            dp[i][0] = True 
        dp[0][stones[0]] = True 
        for i in range(1,n):
            for j in range(target+1):
                if stones[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i]]

        for j in range(target,-1,-1):
            if dp[n-1][j]:
                return sums - j*2
        return 0
    
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 1维DP
        sums = sum(stones)
        target = sums//2 
        n = len(stones)
        if n <= 1:
            return stones[0]
        dp = [False]*(target+1) 
        dp[0] = True 
        for s in stones:
            for j in range(target,s-1,-1):
                dp[j] = dp[j] or dp[j-s]

        for j in range(target,-1,-1):
            if dp[j]:
                return sums-j*2
        return 0
    
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 第二种思路
        # dp[j]表示容量为j的背包能形成的最大价值
        # dp[j] = max(dp[j],dp[j-stones[i]]+stons[i])
        sums = sum(stones)
        target = sums//2 
        n = len(stones)
        if n <= 1:
            return stones[0]
        dp = [0]*(target+1)
        for i in range(n):
            for j in range(target,stones[i]-1,-1):
                dp[j] = max(dp[j],dp[j-stones[i]]+stones[i])
        # 一堆石头的总重量是dp[target]，另一堆就是sum - dp[target]。
        return sums-dp[target]-dp[target]