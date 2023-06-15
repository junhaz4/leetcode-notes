def sumOfAllSubarrays(arr):
  '''
  # brute force
  O(n^2)
  n = len(arr)
  res = 0
  for i in range(n):
    temp = 0
    for j in range(i,n):
      temp += arr[j]
      res += temp
  return res 
  
  # prefix sum
  res = 0
  n = len(arr)
  prefix_sum = [0]*26
  prefix_sum[0] = arr[0]
  for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1]+arr[i]
  res = 0
  for i in range(n):
    temp = 0
    for j in range(i,n):
      if i != 0:
        temp = prefix_sum[j]-prefix_sum[i-1]
      else:
        temp = prefix_sum[j]
      res += temp
  return res
  '''
# Every element arr[i] appears in two types of subsets:
# i)  In subarrays beginning with arr[i]. There are (n-i) such subsets. For example [2] appears in [2] and [2, 3].
# ii) In (n-i)*i subarrays where this element is not first element. For example [2] appears in [1, 2] and [1, 2, 3].
  result = 0
  n = len(arr)
  for i in range(0, n):
      result += (arr[i] * (i+1) * (n-i))
  return result


def numberOfIncreasingSubsequence(arr,k):
  n = len(arr)
  if k > n:
    return 0
  dp = [[0]*n for _ in range(k)] # dp[i][j]=count of increasing subsequences of size i ending at index j
  for i in range(n):
    dp[0][i] = 1
  
  for l in range(1,k):
    for i in range(1,n):
      dp[l][i] = 0
      for j in range(l-1,i):
        if arr[j] < arr[i]:
          dp[l][i] += dp[l-1][j]
  res = 0
  for i in range(k-1,n):
    res += dp[k-1][i]
  return res
# arr = [2,6,4,5,7]
# k = 3
# print(numberOfIncreasingSubsequence(arr,3))


def sortByBits(arr):
  def count_bits(n):
    count = 0
    while n:
      n = n&(n-1)
      count += 1
    return count
  res = sorted(arr,key=lambda n: (count_bits(n),n))
  return res

def isPossible(sx,sy,tx,ty):
  if sx > tx or sy > ty: 
    return False
  while sx <= tx and sy <= ty:
    if tx == sx and ty == sy: 
      return True
    if tx == ty: 
      break
    if tx > ty:
        tx %= ty
    elif ty > tx:
        ty %= tx
    
    if tx == sx: # only change ty
        if (ty-sy) % sx ==0:
            return True
        else:
            return False 
        #return (ty-sy)%sx==0
        
    if ty == sy: # only change tx
        if (tx-sx) % sy == 0:
            return True
        else:
            return False 
  return False 

def minStartValue(nums) -> int:
	n = len(nums)
	prefix = [0]*n
	prefix[0] = nums[0]
	for i in range(1,n):
		prefix[i] = prefix[i-1]+nums[i]
	min_num = min(prefix)
	if min_num < 0:
		return 1-min_num
	else:
		return 1

def nextGreaterElement(n):
  digits = list(str(n))
  i = len(digits) - 1
  while i-1 >= 0 and digits[i] <= digits[i-1]:
    i -= 1
  if i == 0:
    return -1
  j = i
  while j+1 < n and digits[j+1] > digits[j]:
    j += 1
  digits[i-1], digits[j] = digits[j], digits[i-1]
  digits[i:] = digits[i:][::-1]
  ret = int(''.join(digits))
  return ret if ret < 1<<31 else -1

def nextPermutation(nums):
  i = j = len(nums)-1
  while i > 0 and nums[i-1] >= nums[i]:
    i -= 1
  if i== 0:
    return nums[::-1]
  k = i-1
  while nums[j] <= nums[k]:
    j -= 1
  nums[k], nums[j] = nums[j], nums[k]  
  l, r = k+1, len(nums)-1  # reverse the second part
  while l < r:
    nums[l], nums[r] = nums[r], nums[l]
    l +=1 
    r -= 1