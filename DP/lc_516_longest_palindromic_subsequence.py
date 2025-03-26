class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 注意：子序列subsequence可以不是连续的，子串subarray必须是连续的
        # dp[i][j]表示s在[i,j]区间内的最长回文子序列
        # s[i]!=s[j],说明s[i]和s[j]的同时加入 并不能增加[i,j]区间回文子序列的长度，那么分别加入s[i]、s[j]看看哪一个可以组成最长的回文子序列
        # dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # s[i]=s[j], dp[i][j]=dp[i+1][j-1]+2
        # 初始化，递推公式无法计算i=j的情况，所以初始化dp[i][i]=1
        # 遍历顺序,根据递推公式得到从下往上，从左往右
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]