class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] = 到达(i,j)的路径数
        # dp[i][j] = dp[i-1][j] + dp[i][j-1] and obstacleGrid[i][j] != 1
        # dp[0][:] = 1, dp[:][0] = 1 
        # 从左上向右下遍历
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:  # 遇到障碍物时，直接退出循环，后面默认都是0
                dp[i][0] = 1
            else:
                break 
        for j in range(n):
            if obstacleGrid[0][j] == 0:  # 遇到障碍物时，直接退出循环，后面默认都是0
                dp[0][j] = 1
            else:
                break 
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]