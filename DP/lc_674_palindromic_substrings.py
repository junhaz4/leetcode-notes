class Solution:
    def countSubstrings(self, s: str) -> int:
        # two pointer
        # 以每个index，index+1为中心，向左右扩散区寻找回文串
        res = 0
        n = len(s)

        def find(left,right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count 

        for i in range(n):
            res += find(i,i)
            res += find(i,i+1)
        return res 

class Solution:
    def countSubstrings(self, s: str) -> int:
        # 动态规划
        # dp[i][j]=s在[i,j]的这个区间内是回文子串
        # s[i]!=s[j] => dp[i][j]=False
        # s[i]=s[j], 
            # 如果 j-i<=1，说明是a,aa这种，那么dp[i][j]=True
            # 如果j-i >1 & s[i+1][j-1]=True, 那么dp[i][j]=True
        # 初始化，dp[i][j]=False
        # 遍历顺序：首先从递推公式中可以看出，情况三是根据dp[i + 1][j - 1]是否为true，在对dp[i][j]进行赋值true的
        # 所以一定要从下到上，从左到右遍历，这样保证dp[i + 1][j - 1]都是经过计算的
        res = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        res += 1
                        dp[i][j] = True 
                    elif dp[i+1][j-1]:
                        res += 1
                        dp[i][j] = True 
        return res
