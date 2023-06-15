# Q3
def transformArray(A,B):
  n = len(A)
  A.sort()
  B.sort()
  res = True
  N=1000000
  hash_a = [0]*(2*N+2)
  hash_b = [0]*(2*N+2)
  for a in A:
    hash_a[a+N] += 1
  for b in B:
    hash_b[b+N] += 1
  for i in range(0,2*N+2):
    if hash_b[i] < 0:
      res = False
    min_n = min(hash_a[i],hash_b[i])
    hash_a[i] -= min_n
    hash_b[i] -= min_n
    if i < 2*N+1:
      hash_b[i+1] -= hash_a[i]
  '''
  for i in range(2*N+1):
    if hash_a[i] != 0:
      if hash_b[i+1] != hash_a[i]:
        res = False
  '''
  return res
# Q4 lc322 coin change
def umbrealla_p(sizes, requirments):
  if requirments == 0:
    return 0
  n = len(sizes)
  dp = [float("inf")] * (requirments+1)
  dp[0] = 0
  for i in range(1,requirments+1):
    for j in range(n):
      dp[i] = min(dp[i],dp[i-sizes[j]]+1)
  return dp[-1] if dp[-1] != float('inf') else -1
        
# Q5 lc 1444
# dfs+memo+postfixsum
def divide_forest(forest,k):
  m, n = len(forest), len(forest[0])
  mod = 10**9 + 7
  dp = [[0]*(n+1) for _ in range(m+1)]
  for row in range(m-1,-1,-1):
    for col in range(n-1,-1,-1):
      dp[row][col] = dp[row][col+1] + dp[row+1][col]-dp[row+1][col+1] + (forest[row][col] == "A")
  memo = {}
  def dfs(k,row,col):
    if dp[row][col] == 0:
      return 0
    if k == 0:
      return 1
    if (k,row,col) in memo:
      return memo[(k,row,col)]
    res = 0
    # horizotally cut
    for r in range(row+1,m):
      if dp[row][col] -dp[r][col] > 0:
        res = (res + dfs(k-1,r,col))%mod
    # cut vertically
    for c in range(col+1,n):
      if dp[row][col] - dp[row][c] > 0:
        res = (res+dfs(k-1,row,c))%mod
    memo[(k, row, col)] = res
    return res
  
  return dfs(k-1,0,0)
