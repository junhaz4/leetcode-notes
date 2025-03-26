class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointer
        if not s:
            return True
        i = 0
        for c in t:
            if s[i] == c:
                i += 1
                if i == len(s):
                    return True
        return False
    

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # dp[i][j] 表示以下标i-1为结尾的字符串s，和以下标j-1为结尾的字符串t，相同子序列的长度为dp[i][j]。
        # if s[i-1]=t[j-1],dp[i][j] = dp[i - 1][j - 1] + 1;，因为找到了一个相同的字符，相同子序列长度自然要在dp[i-1][j-1]的基础上加1
        # if (s[i - 1] != t[j - 1]),此时相当于t要删除元素，t如果把当前元素t[j - 1]删除，那么dp[i][j] 的数值就是 看s[i - 1]与 t[j - 2]的比较结果了，即：dp[i][j] = dp[i][j - 1];
        # 初始化，dp[i][0]和dp[0][0]需要初始化为0
        # 从前向后遍历
        n1, n2 = len(s), len(t)
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[n1][n2] == len(s)