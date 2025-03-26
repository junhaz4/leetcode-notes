class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 双指针
        # 以每个index，index+1为中心，向左右扩散区寻找回文串
        # 保存一个全局的start和end用于指向最长的回文子串
        # 遍历s，如果当前的回文子串长于全局的，那就更新全局的
        def find(left,right,s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left+1, right  #【)
        start, end = 0, 0
        for i in range(len(s)):
            left, right = find(i,i,s)
            if right-left > end-start:
                end = right 
                start = left 
            left, right = find(i,i+1,s)
            if right-left > end-start:
                end = right 
                start = left 
                
        return s[start:end]
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        # dp[i][j]表示s[i,j]区间的子串是否是回文子串
        # s[i]=s[j], if j-i<=1 dp[i][j]=True, else if dp[i+1][i-1]=True, dp[i][j]=True
        # s[i]!=s[j], dp[i][j] = False
        # 初始化，dp[i][j]不能初始化为true，否则刚开始就全都匹配上了。
        # 遍历顺序从下到上，从左到右
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        start, end = 0, 0
        for i in range(n-1,-1,-1):
            for j in range(n):
                if s[i] == s[j]:
                    if j-i <= 1:
                        dp[i][j] = True 
                    elif dp[i+1][j-1]:
                        dp[i][j] = True 
                if dp[i][j] and j-i+1 > end-start+1:
                    start = i 
                    end = j
        return s[start:end+1]