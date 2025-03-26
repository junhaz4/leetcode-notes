class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子序列为dp[i][j]
        # 递推公式
            # if t1[i-1]==t2[j-1], dp[i][j] = dp[i-1][j-1]+1
            # 否则看看t1[0, i - 2]与t2[0, j - 1]的最长公共子序列dp[i-1][j]
            # t1[0, i - 1]与t2[0, j - 2]的最长公共子序列dp[i][j-1]，取最大的
        # 初始化,dp[i][0]=0, t1[0, i-1]和空串的最长公共子序列自然是0，同理dp[0][j]=0
        # 从前向后遍历，外层text1，内层text2，可以交换顺序
        n1, n2 = len(text1), len(text2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])    
        return dp[n1][n2]


    def longestCommonSubstring(self,text1,text2):
        # dp[i][j]长度为[0, i - 1]的字符串text1与长度为[0, j - 1]的字符串text2的最长公共子串为dp[i][j]
        # 递推公式
            # if t1[i-1]==t2[j-1], dp[i][j] = dp[i-1][j-1]+1
            # 否则 dp[i][j] = 0
        # 初始化，dp[i][0] = 0, dp[0][j] = 0
        # 从前向后遍历，外层text1，内层text2，可以交换顺序
        n1, n2 = len(text1), len(text2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        res = 0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                res = max(res,dp[i][j])
        return res 


