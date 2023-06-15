""" 
线程和进程的区别
如何避免死锁
创建一个线程由几种方式
计算网络体系结构
TCP和UDP的区别
HTTP协议讲一下我讲了HTTP报文的构造——请求头、请求体,讲一下GET和POST的区别        
进程间通信方式
虚拟地址到物理地址映射 mmu
详细问了ARP的实现原理
python 2和python 3 区别
python线程池 内存池, 内存池机制还有垃圾回收,类的概念，怎么初始化类，怎么去复制类
栈和队列的区别
三次握手
"""

## leecode56合并区间
## leecode168、171，execl列名和数字的互相转换
## lc 820, 491
## 然后是LeetCode原题，第92题 反转链表Ⅱ 
## 手撕，**239，滑动窗口最大值
## 手撕：**394，字符串解码
## lc 跳台阶，背包为题
## 手撕代码——合并链表
## 手撕代码——判断链表是否存在环 
## 手撕代码：一个空字符 t ，每次操作可以往字符串t中任意位置放入‘abc’，例如‘a abc  bc’，给你一个字符串 s  判断是否可以通过这样的若干次操作得到。e.g. s= 'abcababcc' ,True
## 手撕代码：接雨水
## 手撕代码 leetcode 12.整数转罗马数字（中等） 数学、哈希表
## 找出字符串中连续元音字母最长的子串
# 给100元去购买肥皂等三类物品，有多少排列组合
## 手撕: 分发子弹 后来查了改自力扣分发糖果 
## 手撕: 841.钥匙和房间,一开始想到的是用set遍历去重…面试官及时提醒用dfs
## 砖墙问题手撕(lc554) 问了下考官说按测试用例输入就行了 所以很快就a了
## 手撕 考官自己文本上写的 给定字符串，按出现次数从高到低排序输出ans 也挺简单的 直接a
## 求整数二进制表示中1的个数
## 给两个非负整数大数求和
## 所有和为target的连续正整数
## 手撕：判断一个自然数是否是某个数的平方
# 手撕：给定字符串，只有小写字母，求其中每个字符都不相等的子串的最长长度
## 无重复字符的最长子串
## 两个字符串的最长公共子串
## leetcode34题
## lc 1540
## 手撕代码 leetcode 455.分发饼干（简单） 贪心
# 算法：给定一个字符串序列和一个数n，输出在字符串序列中出现n次的单词；若多个单词出现n次，输出后一个。如python Java cpp go java go cpp，2，输出go
# 算法：页码显示，对于总页码N < 7显示所有页码，反之则最多只显示7个页码（首页页码、尾页页码、当前页K以及当前页前后两页的页码）；未显示的连续页码用省略号“…”代替。如：N = 94，K = 5，则显示页码1 … 3 4 5 6 7 … 94；N = 94，K = 93，则显示页码1 … 91 92 93 94。输入：两个空格分开的整数N, K(1≤ K ≤ N ≤ 100)，分别表示总页数和当前页。输出：所显示的页码，用空格分开，未显示的连续页码用省略号”…”统一代替。

def leastBricks(self, wall: List[List[int]]) -> int:
    # brick wall
    hash_map = {}
    for row in wall:
        brick = 0
        for i in range(len(row)-1):
            brick += row[i]
            if brick in hash_map:
                hash_map[brick] += 1
            else:
                hash_map[brick] = 1
    n = len(wall)
    res = n
    for key, value in hash_map.items():
        res = min(res,n-value)
    return res

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    '''
    def canVisitAllRooms(self, rooms):
        visited = set([0])
        def dfs(room):
            for neib in rooms[room]:
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib)
        dfs(0)
        return len(visited) == len(rooms)    
    '''
    stack = [0]
    n = len(rooms)
    visited = [False]*n
    visited[0] = True
    while stack:
        room = stack.pop()
        for key in rooms[room]:
            if not visited[key]:
                visited[key] = True
                stack.append(key)
    return all(visited)s

from collections import defaultdict, deque
def findContinuousSequence(self, target: int) -> List[List[int]]:
    #所有和为target的连续正整数
    left, right = 1, 1
    window = 0
    res = []
    while left <= target//2:
        if window > target:
            window -= left
            left += 1
        elif window < target:
            window += right
            right += 1
        else:
            temp = list(range(left,right))
            res.append(temp)
            window -= left
            left += 1
    return res

def getStringFromEmptyString(self, s: str) -> bool:
    # 一个空字符 t ，每次操作可以往字符串t中任意位置放入‘abc’，例如‘a abc  bc’，给你一个字符串 s  判断是否可以通过这样的若干次操作得到
    if len(s) < 3:
        return False
    stack = []
    for char in s:
        stack.append(char)
        if len(stack) >= 3:
            if stack[-1] == "c" and stack[-2] == 'b' and stack[-3] == 'a':
                stack.pop()
                stack.pop()
                stack.pop()
    return not stack

def titleToNumber(columnTitle: str) -> int:
    res = 0
    s = columnTitle
    n = len(s)
    for i in range(n):
        res = res*26
        res += ord(s[i])-ord('A')+1
    return res

def convertToTitle( columnNumber: int) -> str:
    n = columnNumber
    res = ""
    while n > 0:
        n -= 1
        res = chr(n % 26 + ord('A')) + res
        n //= 26
    return res
  
def minimumLengthEncoding(words):
  """
  Build a set of words.
  Iterate on all words and remove all suffixes of every word from the set.
  Finally the set will the set of all encoding words.
  Iterate on the set and return sum(word's length + 1 for every word in the set)
  O(NK^2) for time and 'O(NK)' for space.
  """
  s = set(words)
  for w in words:
      for i in range(1, len(w)):
          s.discard(w[i:])
  return sum(len(w) + 1 for w in s)


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
  que = deque()
  n = len(nums)
  res = []
  if k == 1:
      return nums
  if n*k == 0:
      return []
  # First traversing through K in the nums and only adding maximum value's index to the deque.
  # Note: We are olny storing the index and not the value.
  # Now, Comparing the new value in the nums with the last index value from deque,
  # and if new valus is less, we don't need it
  for i in range(k):
      while que:
          if nums[que[-1]] < nums[i]:
              que.pop()
          else:
              break
      que.append(i)
  # Here we will have deque with index of maximum element for the first subsequence of length k.
  # Now we will traverse from k to the end of array and do 4 things
  # 1. Appending left most indexed value to the result
  # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
  # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
  # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)
  for i in range(k,n):
      res.append(nums[que[0]])
      if que[0] < i-k+1:
          que.popleft()
      while que:
          if nums[que[-1]] < nums[i]:
              que.pop()
          else:
              break
      que.append(i)
      
  res.append(nums[que[0]])
  return res
  
def decodeString(s: str) -> str:
  stack = []
  current_string = ""
  k = 0
  for char in s:
      if char == "[":
          # Just finished parsing this k, save current string and k for when we pop
          stack.append((current_string, k))
          # Reset current_string and k for this new frame
          current_string = ""
          k = 0
      elif char == "]":
          # We have completed this frame, get the last current_string and k from when the frame 
          # opened, which is the k we need to duplicate the current current_string by
          last_string, last_k = stack.pop(-1)
          current_string = last_string + last_k * current_string
      elif char.isdigit():
          k = k * 10 + int(char)
      else:
          current_string += char
  return current_string

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  """
  # reucrsion
  if not list1:
      return list2
  if not list2:
      return list1
  if list1.val <= list2.val:
      list1.next = self.mergeTwoLists(list1.next,list2)
      return list1
  else:
      list2.next = self.mergeTwoLists(list1,list2.next)
      return list2
      """
  dummy = ListNode(-1)
  cur = dummy
  while list1 and list2:
      if list1.val <= list2.val:
          cur.next = list1
          list1 = list1.next
      else:
          cur.next = list2
          list2 = list2.next
      cur = cur.next 
  cur.next = list1 if list1 else list2
  return dummy.next 


def intToRoman(self, num: int) -> str:
  d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
  res = ""
  for i in d:
      res += (num//i) * d[i]
      num %= i
  return res

def romanToInt(self, s):
  roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
  z = 0
  for i in range(0, len(s) - 1):
      if roman[s[i]] < roman[s[i+1]]:
          z -= roman[s[i]]
      else:
          z += roman[s[i]]
  return z + roman[s[-1]]

def isPerfectSquare(self, num: int) -> bool:
  if num < 2:
      return True
  left, right = 2, num//2
  while left <= right:
      mid = left + (right-left)//2
      square = mid*mid
      if square == num:
          return True
      elif square < num:
          left = mid+1
      else:
          right = mid-1
  return False 

def countingbits(self, n: int) -> int:
  total = 0
  while n:
      n = n&(n-1)
      total += 1
  return total

def reverseBetween(self, head, m, n):
  dummy = ListNode(0)
  dummy.next = head
  
  cur, prev = head, dummy
  for _ in range(m - 1):
      cur = cur.next
      prev = prev.next
  
  for _ in xrange(n - m):
      temp = cur.next
      cur.next = temp.next
      temp.next = prev.next
      prev.next = temp

  return dummy.next

def trap(self, height: List[int]) -> int:
  leftheight, rightheight = [0]*len(height), [0]*len(height)
  
  leftheight[0]=height[0]
  for i in range(1,len(height)):
      leftheight[i]=max(leftheight[i-1],height[i])
  rightheight[-1]=height[-1]
  for i in range(len(height)-2,-1,-1):
      rightheight[i]=max(rightheight[i+1],height[i])
  
  result = 0
  for i in range(0,len(height)):
      summ = min(leftheight[i],rightheight[i])-height[i]
      result += summ
  return result

def trap(self, height: List[int]) -> int:
  res = 0
  for i in range(len(height)):
      if i == 0 or i == len(height)-1: 
        continue
      lHight = height[i-1]
      rHight = height[i+1]
      for j in range(i-1):
          if height[j] > lHight:
              lHight = height[j]
      for k in range(i+2,len(height)):
          if height[k] > rHight:
              rHight = height[k]
      res1 = min(lHight,rHight) - height[i]        
      if res1 > 0:
          res += res1
  return res


def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    res = 0
    for i in range(len(s)):
        if res <len(g) and s[i] >= g[res]:  #小饼干先喂饱小胃口
            res += 1
    return res
  
def candy(self, ratings: List[int]) -> int:
  candyVec = [1] * len(ratings)
  for i in range(1, len(ratings)):
      if ratings[i] > ratings[i - 1]:
          candyVec[i] = candyVec[i - 1] + 1
  for j in range(len(ratings) - 2, -1, -1):
      if ratings[j] > ratings[j + 1]:
          candyVec[j] = max(candyVec[j], candyVec[j + 1] + 1)
  return sum(candyVec)

def lengthOfLongestSubstring(self, s: str) -> int:
    # longest substring without repeating characters
    freq_map = {}
    start = 0
    n = len(s)
    max_length = 0
    for end in range(n):
        right_char = s[end]
        if right_char in freq_map:
            start = max(freq_map[right_char]+1,start)
        freq_map[right_char] = end
        max_length = max(max_length,end-start+1)
    return max_length

def lengthOfLIS(self, nums: List[int]) -> int:
    # longest increasing subsequence
    '''
    sub = []
    for num in nums:
        i = bisect_left(sub, num)

        # If num is greater than any element in sub
        if i == len(sub):
            sub.append(num)
        
        # Otherwise, replace the first element in sub greater than or equal to num
        else:
            sub[i] = num
    
    return len(sub)
    '''
    n = len(nums)
    dp = [1]*n
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    return max(dp)
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # dp[i][j]: longest of [0,i] and [0,j]
    # dp[i][j] = dp[i-1][j-1]+1 if text1[i] == text2[j]
    n1, n2 = len(text1), len(text2)
    dp = [[0]*(n2+1) for _ in range(n1+1)]
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
    return dp[-1][-1]
       

def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    # longest increasing path in a matrix 
    m, n = len(matrix), len(matrix[0])
    memo = {}
    res = -1
    prev = -1
    def dfs(r,c,prev):
        if r < 0 or r >= m or c < 0 or c >= n or matrix[r][c] <= prev:
            return 0
        if (r,c) in memo:
            return memo[(r,c)]
        left = dfs(r,c-1,matrix[r][c])
        right = dfs(r,c+1,matrix[r][c])
        up = dfs(r-1,c,matrix[r][c])
        bottom = dfs(r+1,c,matrix[r][c])
        memo[(r,c)] = max(left,right,up,bottom)+1
        return memo[(r,c)]
        
    for r in range(m):
        for c in range(n):
            res = max(res,dfs(r,c,prev))
    return res 


def maximumBinaryString(self, binary: str) -> str:
    #count of 0
    c=0
    #final ans string will contain only one zero.therefore shift the first 0  to c places.Initialize ans string with all 1s
    s = binary
    lst=["1"]*len(s)
    for i in range (0,len(s)):
        if s[i]=="0":
            c+=1
    for i in range (0,len(s)):
    #finding the ist 0
        if s[i]=="0":
            lst[i+c-1]="0"
            return "".join(lst)
    return s

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total//10
            val = total % 10
            new = ListNode(val)
            cur.next = new
            cur = cur.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
    
def searchRange(self, nums: List[int], target: int) -> List[int]:
    # search twice for lower and upper bound
    def binary_search(left,right):
        while left <= right:
            mid = left +(right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1
    left, right = 0, len(nums)-1
    lower = binary_search(left,right)
    if lower == -1:
        return [-1,-1]
    upper = binary_search(left,right)
    while lower >= 1 and nums[lower-1] == nums[lower]:
        lower -= 1
    while upper < len(nums)-1 and nums[upper] == nums[upper+1]:
        upper += 1
    return [lower,upper]

def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort() # children
    s.sort() # cookie
    res = 0
    #这里的局部最优就是大饼干喂给胃口大的，充分利用饼干尺寸喂饱一个，全局最优就是喂饱尽可能多的小孩。
    index = len(s)-1
    for i in range(len(g)-1,-1,-1):
        if index >= 0 and s[index] >= g[i]:
            res += 1
            index -= 1
    return res

def longestBeautifulSubstring(self, word: str) -> int:
    # longest substring of all vowels in order
    ans = ii = 0
    unique = 1
    for i in range(1, len(word)): 
        if word[i-1] > word[i]: 
            ii = i 
            unique = 1
        elif word[i-1] < word[i]: 
            unique += 1
        if unique == 5: 
            ans = max(ans, i-ii+1)
    return ans 

def canConvertString(self, s: str, t: str, k: int) -> bool:
    # convert string to another within k steps
    if len(s) != len(t):
        return False
    
    # We calculate the differences
    diff = defaultdict(int)
    for sc, tc in zip(s, t):
        d = (ord(tc) - ord(sc)) % 26
        if d == 0: 
            continue
        if d > k: 
            return False
        diff[d] += 1
        if ((diff[d] - 1) * 26) + d > k:
            return False
    
    return True