class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]：word1[0:i-1]和word2[0:j-1]达到相等所需要的最少操作次数
        # word1[i-1] = word2[j-1] dp[i][j] = dp[i-1][j-1]
        # word1[i-1] != word2[j-1]
            # 插入：word1增加一个字符，这样word2就可以少匹配一个字符，相当于word2删除一个字符[0,i-1][0,j-2]，即dp[i][j-1]+1
            # 删除：word1删除一个[0,i-2][0,j-1]，即dp[i-1][j]+1
            # 替换：word1替换word1[i-1],使其与word2[j - 1]相同，此时word1[i-1]=word2[j-1], 那么dp[i][j] = dp[i - 1][j - 1] + 1;
        # 初始化dp[i][0]=i, 因为需要把word1转换成空字符串；同理dp[0][j]=j
        # 遍历顺序从上到下，从左到右
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
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[n1][n2]