def quicksortMedianOf3Pivots(array):

  def median(a, b, c):
      if ( a - b) * (c - a) >= 0:
          return a
      elif (b - a) * (c - b) >= 0:
          return b
      else:
          return c
        
  def partition_median(array, leftend, rightend):
      left = array[leftend]
      right = array[rightend-1]
      length = rightend - leftend
      if length % 2 == 0:
          middle = array[leftend + length/2 - 1]
      else:
          middle = array[leftend + length/2]
      pivot = median(left, right, middle)
      pivotindex = array.index(pivot) #only works if all values in array unique
      array[pivotindex] = array[leftend]
      array[leftend] = pivot

      i = leftend + 1
      for j in range(leftend + 1, rightend):
          if array[j] < pivot:
              temp = array[j]
              array[j] = array[i]
              array[i] = temp
              i += 1
      leftendval = array[leftend]
      array[leftend] = array[i-1]
      array[i-1] = leftendval
      return i - 1 

  def quicksort_median(array, leftindex, rightindex):
      global mediancomparison
      if leftindex < rightindex:
          newpivotindex = partition_median(array, leftindex, rightindex)
          mediancomparison += (rightindex - leftindex - 1)
          quicksort_median(array, leftindex, newpivotindex)
          quicksort_median(array, newpivotindex + 1, rightindex)
    
  mediancomparison = 0
  quicksort_median(array, 0, len(array))
  return mediancomparison

def maxEnergy(energy,mat):
  n = 4
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

mat = [[10,20,30,40],
       [60,50,20,80],
       [10,10,10,10],
       [60,50,60,50]]
print(maxEnergy(100,mat))
 
# city attraction
def findBestPath(n, m, max_t, beauty, u, v, t):
  res = 0
  graph = [[] for _ in range(n)]
  def dfs(cur_node, time_taken, beauty_collected, max_t, nodes_passed):
    if time_taken > max_t:
      return
    if cur_node == 0:
      res = max(res,beauty_collected)
    for node, weight in graph[cur_node]:
      added = beauty[node]
      if node in nodes_passed:
        added = 0
      nodes_passed[node] = nodes_passed.get(node,0)+1
      time_taken += weight
      beauty_collected += added
      dfs(node, time_taken, beauty_collected, max_t, nodes_passed) 
      time_taken -= weight
      beauty_collected -= added
      nodes_passed[node] = nodes_passed.get(node,0)-1
      if nodes_passed[node] == 0:
        del nodes_passed[node]
      
  for i in range(m):
    a,b,weight = u[i],v[i],t[i]
    graph[a].append((b,weight))
    graph[b].append((a,weight))
  dfs(0, 0, beauty[0], max_t, {0: 1})
  return res

from collections import defaultdict
def findBestPath(n, m, max_t, beauty, u, v, t):
    def prepare_graph():
        graph = defaultdict(list)
        for i in range(m):
            graph[u[i]].append([v[i], t[i]])
            graph[v[i]].append([u[i], t[i]])
        return graph
    def dfs_helper(node, curr_val, curr_time, visited):
        if curr_time > max_t:
            return
        if node == 0:
            max_beaty[0] = max(max_beaty[0], curr_val)
        for nei in graph[node]:
            new_node, new_node_time = nei[0], nei[1]
            new_node_val = beauty[new_node]
            if new_node in visited:
                new_node_val = 0
            dfs_helper(new_node, curr_val + new_node_val, curr_time + new_node_time, visited | set([new_node]))
    max_beaty = [float('-inf')]
    graph = prepare_graph()

    dfs_helper(0, beauty[0], 0, set([0]))

    return max_beaty[0]