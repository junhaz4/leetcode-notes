def prefix_scores(arr):
  res = []
  cur = 0
  prev = 0
  mode = 10**9+7
  for num in arr:
    cur += num
    res.append(prev+cur)
    prev = res[-1]
  cur_max = 0
  for i in range(len(arr)):
    cur_max = max(cur_max,arr[i])
    res[i] += (i+1)*cur_max
    res[i] %= mode
  return res

def largest_subgrid(grid,maxSum):
  n = len(grid)
  max_sum = 0
  prefix_sum = [[0] * (n + 1) for _ in range(n+ 1)]
  for i in range(1, n+ 1):
    for j in range(1, n+ 1):
      prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + grid[i - 1][j - 1] - prefix_sum[i - 1][j - 1]
  lo, hi = max_sum, n
  for r in range(1, n + 1):
    for c in range(1, n + 1):
        if r + max_sum - 1 > n or c + max_sum - 1 > n: 
          break
        lo = max_sum
        while lo < hi:
          mid = (lo + hi + 1) // 2
          if prefix_sum[r + mid - 1][c + mid - 1] + prefix_sum[r - 1][c + mid - 1] + prefix_sum[r + mid - 1][c - 1] - prefix_sum[r - 1][c - 1] > maxSum:
              hi = mid - 1
          else:
              lo = mid
        max_sum = max(max_sum, lo)
  return max_sum

"""
def findMaxMatrixSize(arr, K):
    n = len(arr)
    m = len(arr[0])
    sum = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m+1):
            if (i == 0 or j == 0):
                sum[i][j] = 0
                continue
            sum[i][j] = arr[i - 1][j - 1] + sum[i - 1][j] + \
                sum[i][j - 1]-sum[i - 1][j - 1]
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i + ans - 1 > n or j + ans - 1 > m):
                break
            mid = ans
            lo = ans
            hi = min(n - i + 1, m - j + 1)
            while (lo < hi):
                mid = (hi + lo + 1) // 2
                if (sum[i + mid - 1][j + mid - 1] +
                    sum[i - 1][j - 1] -
                    sum[i + mid - 1][j - 1] -
                        sum[i - 1][j + mid - 1] <= K):
                    lo = mid
                else:
                    hi = mid - 1
            ans = max(ans, lo)
    return ans
"""

'''
void findMaxMatrixSize(vector<vector<int> > arr, int K)
{
    int i, j;
    int n = arr.size();
    int m = arr[0].size();
    int sum[n + 1][m + 1];
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (i == 0 || j == 0) {
                sum[i][j] = 0;
                continue;
            }
            sum[i][j] = arr[i - 1][j - 1] + sum[i - 1][j]
                        + sum[i][j - 1] - sum[i - 1][j - 1];
        }
    }
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (i + ans - 1 > n || j + ans - 1 > m)
                break;
            int mid, lo = ans;
            int hi = min(n - i + 1, m - j + 1);
            while (lo < hi) {
                mid = (hi + lo + 1) / 2;
                if (sum[i + mid - 1][j + mid - 1]
                        + sum[i - 1][j - 1]
                        - sum[i + mid - 1][j - 1]
                        - sum[i - 1][j + mid - 1]
                    <= K) {
                    lo = mid;
                }
                else {
                    hi = mid - 1;
                }
            }
            ans = max(ans, lo);
        }
    }
    return ans;
}
'''

'''
#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> preSum;
int getSum(int row, int col){
  if(row < 0 || col < 0)
    return 0;
  return preSum[row][col];
}

int sumRegion(int row1, int col1, int row2, int col2) {
  return getSum(row2,col2) - getSum(row1-1,col2) - getSum(row2,col1-1) + getSum(row1-1,col1-1);
}

int largestSubgrid(vector<vector<int>>& grid, int k){
  int n = grid.size();
  preSum.resize(n,vector<int>(n,0));
  for(int i=0; i<n; i++){
    for(int j=0; j<n; j++){
      preSum[i][j] = getSum(i-1,j) + getSum(i,j-1) - getSum(i-1,j-1) + grid[i][j];
    }
  }
  int low = 0, high = n, ans = 0;
  while(low <= high){
    int mid = low + (high - low)/2;
    if(mid == 0)
    return 0;
    bool stop = false;
    for(int i=mid-1; i<n && !stop; i++){
      for(int j=mid-1; j<n && !stop; j++){
        int subSum = sumRegion(i-mid+1,j-mid+1,i,j);
        if(subSum > k){
          stop = true;
        }
      }
    }
    if(stop){
      high = mid - 1;
    }
    else{
      ans = mid;
      low = mid + 1;
    }
  }
  return ans;
}
'''

def getMaxOrSum(arr, k):
  n = len(arr)
  if n==1:
      return arr[0]<<k
  pre = [0]*n
  post = [0]*n
  # From the FRONT of the array bitwise-or of each element with its next ARR element and store in array PRE
  pre[0] = arr[0]
  for i in range(1,n):
      pre[i] = pre[i-1] | arr[i]
  # From the BACK of the array bitwise-or of each element with its previous ARR element and store in array POST
  post[n-1] = arr[n-1]
  for i in range(n-2,-1,-1):
      post[i] = post[i+1] | arr[i]
  last_max = arr[0] << k | post[1]
  front_max = arr[n-1] << k | pre[n-2]
  ans = max(last_max, front_max)
  for i in range(1, n-1):
      ans = max(ans, (arr[i]<<k) | pre[i-1]| post[i+1])
  return ans

def assigned_parking(x,y):
  n = len(x)
  x.sort()
  for i in range(n):
      x[i] -= i
  y.sort()
  x.sort()
  fuel = 0
  for i in range(n):
      fuel += abs(y[i] - y[n//2])
      fuel += abs(x[i] - x[n//2])
  return fuel

def queue_at_atm(k,amount):
  assert 1 <= len(amount) <= 10 ** 5
  assert all(1 <= x <= 10 ** 9 for x in amount)
  assert 1 <= k <= 10 ** 6

  arr = []
  for i in range(len(amount)):
      arr.append([(amount[i] + k - 1) // k, i + 1])

  arr.sort()
  arr2 = [x[1] for x in arr]
  return arr2

def palindrome_subsequence(s):
  assert 5 <= len(s) <= 10**5
  assert all(x == '0' or x == '1' for x in s)
  # initialize variables
  n = len(s)
  pre_cnt, suf_cnt = [0] * 4, [0] * 4
  cnt, cnt_so_far = [0, 0], [0, 0]
  s = [0 if x =='0' else 1 for x in s]
  mod, ans = 10 ** 9 + 7, 0
  for j in range(n):
      suf_cnt[s[j]] += cnt[0]
      suf_cnt[2 + s[j]] += cnt[1]
      cnt[s[j]] += 1
  for j in range(n):
      cnt[s[j]] -= 1
      suf_cnt[2 * s[j]] -= cnt[0]
      suf_cnt[2 * s[j] + 1] -= cnt[1]
      ans += pre_cnt[0] * suf_cnt[0] # "00" and "00"
      ans += pre_cnt[1] * suf_cnt[2] # "01" and "10"
      ans += pre_cnt[2] * suf_cnt[1] # "10" and "01"
      ans += pre_cnt[3] * suf_cnt[3] # "11" and "11"
      ans %= mod
      pre_cnt[s[j]] += cnt_so_far[0]
      pre_cnt[2 + s[j]] += cnt_so_far[1]
      cnt_so_far[s[j]] += 1
  return ans
  

def reaching_points(x1,y1,x2,y2):
  while x1 <= x2 and y1 <= y2:
    if x1 == x2 and y1 == y2:
      return True
    if x2 == y2:
      break
    if x2 > y2:
      x2 %= y2
    elif y2 > x2:
      y2 %= x2
    
    if x1 == x2:
      if (y2-y1)%x1 == 0:
        return True
      else:
        return False
    if y1 == y2:
      if (x2-x1)%y1 == 0:
        return True
      else:
        return False
  """
  while tx >= sx and ty >= sy:
    if tx == ty:
        break
    elif tx > ty:
        if ty > sy:
            tx %= ty
        else:
            return (tx - sx) % ty == 0
    else:
        if tx > sx:
            ty %= tx
        else:
            return (ty - sy) % tx == 0
  return tx == sx and ty == sy
  """
  return False

def split_array(nums):
  mod = 10**9+7
  n = len(nums)
  prefix = [0]*n 
  prefix[0] = nums[0]
  for i in range(1,n):
    prefix[i] = prefix[i-1] + nums[i]
  res = 0
  def is_valid(i,j):
    s1 = prefix[i]
    s2 = prefix[j]-prefix[i]
    s3 = prefix[-1]-prefix[j]
    if s2 <= s1+s3:
      return True
    return False
  for i in range(0,n-1):
    left, right = i+1, n-2
    while left + 1 < right:
      mid = left + (right-left)//2
      # mid = (left+right)//2
      if is_valid(i,mid):
        left = mid
      else:
        right = mid
    if is_valid(i,right):
      res += right-i
    elif is_valid(i,left):
      res += left-i
    res %= mod
  return res
print(split_array([1,2,3,4]))

def purchasing_supplies(scenarios):
  info = []
  for s in range(scenarios):
    info.append(list(map(int,s.split(' '))))
  for i in info:
    budget = i[0]
    cost = i[i]
    amount = i[2]
    containers = budget//cost
    res = containers
    while True:
      res += containers//amount
      containers = containers//amount + containers%amount
      if containers >0 and containers < amount:
        break
  return res

def segment_sort(arr):
  n_arr = sorted(arr)
  n1, n2 = 0, 0
  res = 0
  for a, b in zip(n_arr,arr):
    n1 += a
    n2 += b
    res += (n1 == n2)
  '''
  stack = []
  for num in arr:
      largest = num
      while stack and stack[-1] > num:
          largest = max(largest, stack.pop())
      stack.append(largest)
  
  return len(stack)
  '''
  '''
  n = len(arr)
  suffix_min = [0] * (n + 1)
  suffix_min[n] = float("inf")
  for i in range(n - 1, -1, -1):
      suffix_min[i] = min(suffix_min[i + 1], arr[i])
  prefix_max_value = -1
  res = 0
  for idx, val in enumerate(arr):
      prefix_max_value = max(prefix_max_value, val)
      if (prefix_max_value <= suffix_min[idx + 1]):
          res += 1
  return res
  '''
  return res

def matrix_traversal(mat):
  n = 4
  energy = 100
  dp = [[float("inf")]*4 for _ in range(4)]
  for i in range(n):
    for j in range(n):
      if i == 0:
        dp[i][j] = 0
  for i in range(n-1):
    for j in range(n):
      if j >= 1:
        dp[i + 1][j - 1] = min(dp[i + 1][j - 1], mat[i][j] + dp[i][j])
      if j + 1 < n:
        dp[i + 1][j + 1] = min(dp[i + 1][j + 1], mat[i][j] + dp[i][j])
      dp[i + 1][j] = min(dp[i + 1][j], mat[i][j] + dp[i][j])
  res = float("inf")
  for i in range(n):
    res = min(res,mat[3][j] + dp[3][j])
  return energy-res


def distinct_order_traversal(g_nodes,g_from,g_to):
  '''
  def addEdge(v, w):
    global visited, adj
    adj[v].append(w)
    adj[w].append(v)
    
  def BFS(componentNum, src):
    global visited, adj
    # Mark all the vertices as not visited
    # Create a queue for BFS
    #a = visited
    queue = deque()
    queue.append(src)
    # Assign Component Number
    visited[src] = 1
    # Vector to store all the reachable
    # nodes from 'src'
    reachableNodes = []
    while (len(queue) > 0):
        # Dequeue a vertex from queue
        u = queue.popleft()
        reachableNodes.append(u)
        # Get all adjacent vertices of the dequeued
        # vertex u. If a adjacent has not been visited,
        # then mark it visited and enqueue it
        for itr in adj[u]:
            if (visited[itr] == 0):
                # Assign Component Number to all the
                # reachable nodes
                visited[itr] = 1
                queue.append(itr)
    return reachableNodes
  def displayReachableNodes(m):
      for i in m:
          print(i, end = " ")
      print()
      
  def findReachableNodes(arr, n):
    global V, adj, visited
    # Get the number of nodes in the graph
    # Map to store list of reachable Nodes for a
    # given node.
    a = []
    # Initialize component Number with 0
    componentNum = 0
    # For each node in arr[] find reachable Nodes
    for i in range(n):
        u = arr[i]
        # Visit all the nodes of the component
        if (visited[u] == 0):
            componentNum += 1
            # Store the reachable Nodes corresponding
            # to the node 'i'
            a = BFS(componentNum, u)
        # At this point, we have all reachable nodes

        # from u, print them by doing a look up in map m.
    return a

# Driver code
if __name__ == '__main__':
    V = 7
    adj = [[] for i in range(V + 1)]
    visited = [0 for i in range(V + 1)]
    addEdge(1, 2)
    addEdge(2, 3)
    addEdge(3, 4)
    addEdge(3, 1)
    addEdge(5, 6)
    addEdge(5, 7)
    # For every ith element in the arr
    # find all reachable nodes from query[i]
    arr = [ 2, 4, 5 ]
    # Find number of elements in Set
    n = len(arr)
    findReachableNodes(arr, n)
  '''

def decode_string(s):
  n = len(s)
  i = 0
  num = 0
  stack = [""]
  while i < n:
    if s[i].isdigit():
      num = num*10 + int(s[i])
    elif s[i] == "[":
      stack.append(num)
      num = 0
      stack.append("")
    elif s[i] == "]":
      s1 = stack.pop()
      count = stack.pop()
      s2 = stack.pop()
      stack.append(s2+s1*count)
    else:
      stack[-1]+=s[i]
    i+=1
  return "".join(stack)
