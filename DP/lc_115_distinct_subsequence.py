class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j]以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]。
        # 递推公式dp[i][j]
            # s[i-1]=t[j-1]，可以分成两种情况
                # 不让 s【i-1】 参与匹配，也就是需要让 s 中 【0,i-2】个字符去匹配 t 中的 【0,j-1】字符。此时匹配值为 f【i-1】【j】
                # 让 s【i-1】 参与匹配，这时候只需要让 s 中 【0,i-2】个字符去匹配 t 中的 【0,j-2】字符即，同时满足 s【i-1】=t【j-1】。此时匹配值为 dp【i-1】【j-1】
                # 举例，假设当前遍历到的 t 是 bag，s 是 babga，此时 s 又来了一个 g， 和当前 t 的最后一个元素相同了。
                # 这个时候新的 babgag 含有 bag 的数量是在 babga 原本包含的 bag 数量（dp【i - 1】【j】）的基础上，
                # 增加了使用新来的 g 新组成的 bag 数量。新来的 g 能组成多少个bag，其实是原本的 babga 包含多少个 ba。也就是 dp【i - 1】【j - 1】。
            # s[i-1]!=t[j-1]，不使用s[i-1]进行匹配，而是使用s[i-2]和t[j-1]匹配的结果，那么就是s[i-1][j]
        # 初始化 
            # dp[i][0]以i-1为结尾的s可以随便删除元素，出现空字符串的个数, dp[i][0] = 1
            # dp[0][j]空字符串s可以随便删除元素，出现以j-1为结尾的字符串t的个数 dp[0][j] = 0
            # dp[0][0] = 1
        # 遍历顺序，从上到下，从左到右进行遍历
        n1, n2 = len(s), len(t)
        if n2 > n1:
            return 0
        dp = [[0]*(n2+1) for _ in range(n1+2)]
        for i in range(n1+1):
            dp[i][0] = 1
        for j in range(1,n2+1):
            dp[0][j] = 0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j]+ dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n1][n2]
    
        
        # 递归
        # 从尾部向前进行递归
        @cache
        def dfs(i, j):
            if i < 0 and j < 0:
                return 1
            if i < 0 or i < j :
                return 0
            if j < 0:
                return 1
            if s[i] == t[j]:
                return dfs(i-1, j-1) + dfs(i-1, j)
            return dfs(i-1, j)
        
        m, n = len(s), len(t)
        MAX = 10**9 + 7
        ans = dfs(m-1, n-1) % MAX
        return ans