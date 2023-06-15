# method 1 brute force
# one for loop to pick the end of the substring and another for loop to compare 
# time complexity: O(n^2) space complexity: O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        res = False
        half = n//2 # 4//2=2, 3//2=1
        for i in range(1,half+1):
            sub = s[:i]
            for j in range(0, len(s), len(sub)):
                if sub != s[j:j+len(sub)]:
                    res = False
                    break
            else:
                res = True
                break
        return res
  
# Method 2 
# 移动匹配: 只要两个s拼接在一起，要刨除 s + s 的首字符和尾字符，这样避免在s+s中搜索出原来的s, 里面还出现一个s的话, 说明是又重复子串组成
# time: O(n^2) space O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s+s
        t = t[1:-1]
        return s in t

# Method 3
# KMP
# time O(n) space O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = 0
        n = len(s)
        nxt = [0]*n
        for i in range(1,n):
            while j > 0 and s[i] != s[j]:
                j = nxt[j-1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        if nxt[-1] != 0 and n % (n-nxt[-1]) == 0:
            return True
        return False