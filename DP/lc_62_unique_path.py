class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = 从原点到（i，j)的路径数
        # 因为只能向下或者向右走，dp[i][j] = dp[i][j-1]+dp[i-1][j]
        # 第一行和第一列的点都只有一条路径能到达
        # 从左上向着右下角遍历
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]