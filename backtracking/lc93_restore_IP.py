class Solution:
    def restoreIpAddresses(self, s: str) ->list[str]:
        self.result = []
        def backtracking(s,startIndex,nums):
            if nums==3:
                if is_valid(s,startIndex,len(s)-1):
                    self.result.append(s)
                    return
                for i in range(startIndex,len(s)):
                    if is_valid(s,startIndex,i):
                        s=s[:i+1]+'.'+s[i+1:]
                        nums+=1
                        backtracking(s,i+2,nums)
                        nums-=1
                        s=s[:i+1]+s[i+2:]
                    else:
                        continue
        def is_valid(s,start,end):
            if start > end:
                return False 
            if start != end and s[start]=='0':
                return False
            if not 0<=int(s[start:end+1])<=255:
                return False 
            return True
        backtracking(s,0,0)
        return self.result 