class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]：以i-1为结尾的字符串word1，和以j-1位结尾的字符串word2，想要达到相等，所需要删除元素的最少次数。
        # 当word1[i - 1] 与 word2[j - 1]相同的时候，dp[i][j] = dp[i - 1][j - 1];
        # 当word1[i - 1] 与 word2[j - 1]不相同的时候，有三种情况：
            # 情况一：删word1[i - 1]，最少操作次数为dp[i - 1][j] + 1
            # 情况二：删word2[j - 1]，最少操作次数为dp[i][j - 1] + 1
            # 情况三：同时删word1[i - 1]和word2[j - 1]，操作的最少次数为dp[i - 1][j - 1] + 2
            # dp[i][j] = min({dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1})
            # 注意：dp[i][j - 1] + 1 = dp[i - 1][j - 1] + 2
            # 解释：dp[i][j-1]如果将word1[i-1]删除了，就变成了dp[i-1][j-1], dp[i][j-1]=dp[i-1][j-1]+1
            # 或者说情况三同时删除已经被包含在了情况一和情况二中  
        # 初始化dp[i][0]=i,word2此时为空字符串，word1需要所有的才能和空串一致 同理dp[0][j]=j  

        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    #dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
                    dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1)
        return dp[n1][n2]
    

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 思路二，这道题可以转换成求word1和Word2的最长公共子序列，除了最长公共子序列的元素其他的都要删除
        n1, n2 = len(word1), len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+2):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return n1+n2-2*dp[n1][n2]