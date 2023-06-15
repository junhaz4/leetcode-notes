# Method 1 Brute Force
# iterate through the whole string and check every substring of the same length as needle

class Solution(object):
  def strStr(self, haystack, needle):
    res = -1
    for i in range(len(haystack)):
      if haystack[i:i+len(needle)] == needle:
        res = i
        break
    return res

# Method 2 KMP
# next array 整体减一
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a=len(needle)
        b=len(haystack)
        if a==0:
            return 0
        next=self.getnext(a,needle)
        p=-1
        for j in range(b):
            while p>=0 and needle[p+1]!=haystack[j]:
                p=next[p]
            if needle[p+1]==haystack[j]:
                p+=1
            if p==a-1:
                return j-a+1
        return -1

    def getnext(self,a,needle):
        next=['' for i in range(a)]
        j = -1
        next[0]=j
        for i in range(1,len(needle)):
            while (j >= 0 and needle[j+1]!=needle[i]):
                j = next[j]
            if needle[j+1]==needle[i]:
                j += 1
            next[i]=j
        return next
      
# next array保持原样
    def strStr(self, haystack: str, needle: str) -> int:
        a=len(needle)
        b=len(haystack)
        if a==0:
            return 0
        next=self.getnext(a,needle)
        p = 0
        for j in range(b):
            while p>0 and needle[p]!=haystack[j]:
                p=next[p-1]
            if needle[p]==haystack[j]:
                p+=1
            if p==a:
                return j-a+1
        return -1

    def getnext(self,a,needle):
        next=['' for i in range(a)]
        j = 0
        next[0]=0
        for i in range(1,len(needle)):
            while (j > 0 and needle[j]!=needle[i]):
                j = next[j-1]
            if needle[j]==needle[i]:
                j += 1
            next[i]=j
        return next