class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 回溯法
        def backtracking(s,startIndex,wordSet):
            if startIndex == len(s):
                return True
            if startIndex in memo: # 如果memory[startIndex]不是初始值了，直接使用memory[startIndex]的结果
               return memo[startIndex] 
            for i in range(startIndex,len(s)):
                word = s[startIndex:i+1] # 截取子串
                if word in wordSet and backtracking(s, i + 1, wordSet):
                    return True
            memo[startIndex] = False # 记录以startIndex开始的子串是不可以被拆分的
            return False
        
        @functools.cache
        def dfs(s: str, start: int):
            if start == len(s):
                return True
            for i in range(start, len(s)):
                if s[start: i + 1] in wordDict and dfs(s, i + 1):
                    return True
            return False
        #return dfs(s, 0)

        wordSet = set(wordDict)
        startIndex = 0
        memo = {} # 保存每次计算的以startIndex起始的计算结果
        return backtracking(s,startIndex,wordSet)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 动态规划
        # dp[i] : 字符串长度为i的话，dp[i]为true，表示可以拆分为一个或多个在字典中出现的单词。
        # 如何确定dp[i]为True? 如果dp[j]=True and [j,i]区间出现在wordDict中，则说明dp[i]=True
        # 初始化dp[0] = True
        wordSet = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True 
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet: # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    dp[i] = True 
                    break
        return dp[n]
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 优化空间，只记录为True的位置
        n = len(s)
        wordSet = set(wordDict)
        trues = [0]
        for j in range(1, n+1):
            for i in trues:
                if s[i:j] in wordSet:
                    trues.append(j)
                    break
        return trues[-1] == len(s)