class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # strs是物品，m和n是背包，不同长度的字符串就是不同大小的待装物品
        # dp[i][j]表示最多i个0和j个1的最大子集的长度
        # dp[i][j]可以由前一个strs里的字符串推导出来，strs里的字符串有zeroNum个0，oneNum个1。
        # dp[i][j] = dp[i-zeroNum][j-oneNum]+1
        # 初始化
        # 先遍历strs，统计每个str中1和0的数量，然后从后向前遍历背包容量
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            oneNum = s.count("1")
            zeroNum = s.count("0")
            for i in range(m,zeroNum-1,-1):
                for j in range(n,oneNum-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-zeroNum][j-oneNum]+1)
        return dp[m][n]