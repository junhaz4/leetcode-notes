# Condensed List
from collections import defaultdict
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def condenst_list(head):
  if not head:
      return None
  node_dict = defaultdict(int)
  cur = head
  while cur:
      node_dict[cur.val] += 1
      cur = cur.next
  dummy = ListNode(-1,next=head)
  prev = dummy
  while head:
      if node_dict[head.val] > 1:
          prev.next = head.next
      else:
          prev = prev.next
      head = head.next
  return dummy.next

# Remove All Adjacent Duplicates in String II / Word Compression 
def removeDuplicates(s,k):
  """
  stack = [] # [char,count]
  for char in s:
      if stack and stack[-1][0] == char:
          stack[-1][1] += 1
      else:
          stack.append([char,1])
      if stack[-1][1] == k:
          stack.pop()
  return ''.join([c*f for c, f in stack])
  """
  stack = [['#', 0]] # [char,count]
  for c in s:
      if stack[-1][0] == c:
          stack[-1][1] += 1
          if stack[-1][1] == k:
              stack.pop()
      else:
          stack.append([c, 1])
  return ''.join(c * k for c, k in stack)
  
# cut metal
def maxProfit(costPerCut, salePrice, lengths):
  max_profit = 0
  for sale_length in range(1, max(lengths) + 1):
    sale_price_per_rod = salePrice * sale_length
    profit = 0
    for rod_length in lengths:
        uniform_rods = rod_length // sale_length
        if uniform_rods > 0:
            extra_cut = 1 if rod_length % sale_length > 0 else 0
            total_cuts = uniform_rods - 1 + extra_cut
            costs = total_cuts * costPerCut
            revenues = uniform_rods * sale_price_per_rod
            if revenues > costs:
                profit += revenues - costs
    if profit > max_profit:
        max_profit = profit
  return max_profit 

# is possible 
def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
  while tx >= sx and ty >= sy:
      if tx == ty:
          break
      elif tx > ty:
          if ty > sy:
              tx = tx%ty
          else:
              return (tx-sx)%ty == 0
      else:
          if tx > sx:
              ty = ty%tx
          else:
              return (ty-sy)%tx == 0
  return tx == sx and ty == sy

# football scores
def football_socres(teamA,teamB):
  res = []
  teamA.sort()
  for score in teamB:
    left, right = 0, len(teamA)-1
    while left <= right:
      mid = left + (right-left)//2
      if teamA[mid] > score:
        right = mid-1
      else:
        left = mid+1
    res.append(left) #  find the first index of an element in A strictly greater than that element in B
  return res

# break palindrome
def breakPalindrome(self, palindrome: str) -> str:
  if len(palindrome) == 1:
      return ''
  for i in range(len(palindrome)//2):
      if palindrome[i] != 'a':
          return palindrome[:i] + "a" + palindrome[i+1:]
  return palindrome[:-1]+'b'

# cardinality sorting
import heapq
def sortBits(array):
  res = []
  def countbits(n):
    count = 0
    while n:
      n = n&(n-1)
      count += 1
      n >>= 1
    return count 
  for n in array:
    ones = countbits(n)
    res.append((ones,n))
  heapq.heapify(res)
  ans = []
  while res:
    ans.append(heapq.heappop(res)[1])
  return ans

# palindrome counter
def countSubstrings(self, s: str) -> int:
  N = len(s)
  result = 0
  # could have 2n-1 possible centers
  for i in range(2*N-1):
      left = i//2
      right = (i+1)//2
      while left >= 0 and right < N and s[left] == s[right]:
          result += 1
          left -= 1
          right += 1
  
  return result

# paris of songs/whole minute delima
def numPairsDivisibleBy60(time) -> int:
  res = 0
  count = [0]*60
  for t in time:
      if t%60 == 0:
          res += count[0]
      else:
          res += count[60-t%60]
      count[t%60] += 1
  return res

# hom many sentence
def countSentences(wordSet, sentences):
  '''
  dic = defaultdict(int)
  for word in wordSet:
      word = ''.join(sorted(word))
      dic[word] += 1
  res =[]
  for sent  in sentences:
      words = sent.split(' ')
      count = 1
      for word in words:
          k = ''.join(sorted(word))
          if k in dic:
            count *= dic[k]
    res.append(count)
  eturn res
'''
  word_map = defaultdict(int)
  for word in wordSet:
    tmp = tuple(sorted(word))
    word_map[tmp] = word_map.get(tmp, 0) + 1
  ans = [1] * len(sentences)
  for i in range(len(sentences)):
    for word in sentences[i].split():
       key = tuple(sorted(word))
       if key in word_map:
          ans[i] *= word_map[key]
    return ans

# lottery coupon
def lotteryCoupon(n):
  if n < 10:
    return n 
  res = []
  for i in range(n):
    temp = i+1
    digit = 0
    while temp > 0:
      digit += temp%10
      temp = temp//10
    res.append(digit)
  winner_dict = dict()
  for i in res:
    if i not in winner_dict:
      winner_dict[i] = 1
    else:
      winner_dict[i] += 1
  result = 0
  max_num = 0
  for value in winner_dict.values():
    if value > max_num:
      max_num = value
      result = 0
    if value == max_num:
      result += 1
  return result

def perfect_team(strings):
  s1 = "pcmbzpcmbz"
  s2 = "mppzbmbpzcbmpbmczcz"
  s3 = "pcmbz"
  s4 = "pcmpp"
  s5 = "pcmpcmbbbzz"
  def solve(word):
    data = {
        "p":0,
        "c":0,
        "m":0,
        "b":0,
        "z":0
    }
    min_val = 99999999
    for char in word:
        data[char] += 1
    for key in data:
        if data[key] <= min_val:
            min_val = data[key]
    return min_val
  
# check two strings are almost equivalent
def checkAlmostEquivalent(word1: str, word2: str) -> bool:
  d={}
  for ch in word1:
      d[ch]=d.get(ch,0)+1
  for ch in word2:
      d[ch]=d.get(ch,0)-1
  difFreq=max(abs(val) for val in d.values())
  return difFreq<=3

# number of palindromic subsequences of length 5 in binary string
def solve(s):
  n = len(s)
  ans = 0
  dp = [[0]*n for _ in range(n)]
  for i in range(n-2,-1,-1):
    for j in range(i+2,n):
      if dp[i + 1][j] == dp[i + 1][j-1]:
        dp[i][j] = dp[i][j-1]
      else:
        dp[i][j] = dp[i][j-1] + dp[i + 1][j] - dp[i + 1][j - 1]
      if s[i] == s[j]:
        dp[i][j] += j - i - 1
  for i in range(n):
    for j in range(i+4,n):
      if s[i] == s[j]:
        ans += dp[i + 1][j - 1]
  return ans

# find number of pairs with given sum in an array
import bisect
def getpaircount(arr,target):
  """n = len(arr)
  arr.sort()
  x, c = 0, 0
  for i in range(n-1):
    x = target-arr[i]
    # upper bound
    y = bisect.bisect_left(arr, x, i+1, n)
    # lower bound
    z = bisect.bisect(arr, x, i+1, n)
    c = c+z-y
  return c"""
  n = len(arr)
  mp = {}
  count = 0
  for i in range(n):
    if target - arr[i] in mp:
      count += mp[target-arr[i]]
    if arr[i] in mp:
      mp[arr[i]] += 1
    else:
      mp[arr[i]] = 1
  return count

# reverse the string without each word
def reverseString(string):
  cur_word = ''
  words = []
  res = ''
  for i in range(len(string)):
    if string[i] == '.':
      words.append(cur_word)
      cur_word = ''
    else:
      cur_word += string[i]
  words.append(cur_word)
  n = len(words)
  for i in range(n-1,-1,-1):
    res += words[i]
    if i != 0:
      res += '.'
  return res

# meadering array
def meandering(unsorted):
    from math import floor
    result = []
    a = sorted(unsorted)
    if len(a) % 2 == 0:
        for x, y in zip(list(reversed(a))[: int(len(a) / 2)], a[:int(len(a) / 2)]):
            result.append(x)
            result.append(y)
    else:
        for x, y in zip(list(reversed(a))[: floor(len(a) / 2)], a[: floor(len(a) / 2)]):
            result.append(x)
            result.append(y)
        result.append(a[floor(len(a) / 2)])
    return result

#Press A for Caps Lock
def pressAforCapsLock(s):
    if not s:
        return None

    if len(s) == 1:
        if s == 'A' or s == 'a':
            return None
        else:
            return s

    # Caps Lock key is initially toggled off
    capslock = False
    result = ""

    for char in s:

        if char == 'A' or char == 'a':
            capslock = not capslock
            continue

        if capslock:
            if ord(char) >= 65 and ord(char) <= 90:
                # Upper Case
                result += chr(ord(char) + 32)

            elif ord(char) >= 97 and ord(char) <= 122:
                # Lower Case
                result += chr(ord(char) - 32)
            else:
                result += char
        else:
            result += char

    return result
  
  # "Maximum Difference in an Array.
def maxDifferenceOddEven(arr):
  result = -1

  length = len(arr)
  for j in range(length):

      right = arr[j]
      for i in range(j):

          if arr[i] < right and arr[i] % 2 == 1 and right % 2 == 0:
              diff = right - arr[i]

              if diff > result:
                  result = diff
  return result

# share purchase
# method 1
def isValid (dic):
  return dic.get('A',0) and dic.get('B', 0) and dic.get('C', 0)

def compute(s):
  counter, length = 0, len(s)
  l,r = 0, length-1
  dic = {}

  for i in range(length):
    if(not dic.get(s[i], False)):
      dic[s[i]] = 1
    else:
      dic[s[i]] += 1
  
  while(isValid(dic)):
    while(isValid(dic)):
      counter += 1
      dic[s[r]] -= 1
      r -= 1
  
    r += 1
    dic[s[l]] -= 1
    l += 1
  
    while(r < length):
      dic[s[r]] += 1
      if(isValid(dic)):
        counter += 1
      r += 1
  
    r -= 1
    dic[s[l]] -= 1
    l += 1
  return counter
# method 2
def compute(s):
  dic = {'A':[], 'B':[], 'C':[]}
  result = 0
  length = len(s)

  # added in reverse order to allow pop() to be O(1)
  for i in range(len(s)-1,-1,-1):
    if (s[i] in dic.keys()):
      dic[s[i]].append(i)
  
  for i in range (length):
    vals = list(map(lambda x:x[-1], dic.values()));
    maxVal = max(vals)
    minVal = min(vals)
    result += (len(s) - maxVal)
    if (i == minVal):
      if (dic['A'][-1] == minVal):
        dic['A'].pop()
        if (len(dic['A']) == 0):
          break;
      elif (dic['B'][-1] == minVal):
        dic['B'].pop()
        if (len(dic['B']) == 0):
          break;
      elif (dic['C'][-1] == minVal):
        dic['C'].pop()
        if (len(dic['C']) == 0):
          break;
  return result

# maximum substring
def lastSubstring(s: str):
  '''
  n = len(s)
  cmax = max(s)
  
  candidates = [i for i, c in enumerate(s) if c == cmax]
  offset = 1
  
  while len(candidates) > 1:
      new_candidates = []
      cmax = max(s[i + offset] for i in candidates if i + offset < n)
      
      for i, st in enumerate(candidates):
          if i > 0 and candidates[i - 1] + offset == st:
              continue
          
          if st + offset < n and s[st + offset] == cmax:
              new_candidates.append(st)
          
      candidates = new_candidates
      offset += 1
  return s[candidates[0]:]
  '''
  n = len(s)
  i, j, k = 0, 1, 0
  while j + k < n:
    k = 0
    while s[i+k] == s[j+k]:
      k += 1
      if j + k == s.length:
        break
    if s[i+k] > s[j+k]:
       j = j + 1 + k
    elif s[i+k] < s[j+k]:
       i = i + 1 + k
    if i >= j:
      j = i + 1
  return s[i:]

# k diff paris in array
class Solution:
    def findPairs(self, nums, k: int) -> int:
      nums = sorted(nums)
      left = 0
      right = 1
      result = 0
      while (left < len(nums) and right < len(nums)):
          if (left == right or nums[right] - nums[left] < k):
              # List item 1 in the text
              right += 1
          elif nums[right] - nums[left] > k:
              # List item 2 in the text
              left += 1
          else:
              # List item 3 in the text
              left += 1
              result += 1
              while (left < len(nums) and nums[left] == nums[left - 1]):
                  left += 1
      return result
    
# group anagrams
def groupAnagrams(self, strs):
  count = defaultdict(list)
  for s in strs:
      freq = [0]*26
      for c in s:
          freq[ord(c)-ord("a")] += 1
      count[tuple(freq)].append(s)
  return count.values()

# find all anagrams in a string given a target string
def findAnagrams(s: str, p: str):
    ns, np = len(s), len(p)
    if ns < np:
        return []

    p_count, s_count = [0] * 26, [0] * 26
    # build reference array using string p
    for ch in p:
        p_count[ord(ch) - ord('a')] += 1
    
    output = []
    # sliding window on the string s
    for i in range(ns):
        # add one more letter 
        # on the right side of the window
        s_count[ord(s[i]) - ord('a')] += 1
        # remove one letter 
        # from the left side of the window
        if i >= np:
            s_count[ord(s[i - np]) - ord('a')] -= 1
        # compare array in the sliding window
        # with the reference array
        if p_count == s_count:
            output.append(i - np + 1)
    
    return output

# count binary substring with same number of 0 and 1
def countBinarySubstrings(self, s):
  ans, prev, cur = 0, 0, 1
  for i in range(1, len(s)):
      if s[i-1] != s[i]:
          ans += min(prev, cur)
          prev, cur = cur, 1
      else:
          cur += 1
  return ans + min(prev, cur)