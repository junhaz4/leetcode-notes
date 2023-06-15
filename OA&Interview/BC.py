def f(pnl,k):
  res = float('-inf')
  window = 0
  start = 0
  for end in range(len(pnl)):
    window += pnl[end]
    while end-start+1 > k:
      window -= pnl[start]
      start += 1
    res = max(res,window)
  return res 

#pnl = [-3,4,3,-2,2,5]
#k = 4
# 8
# pnl = [4,3,-2,9,-4,2,7]
# k = 6
# 15
##pnl=[2,5,-7,8,-6,4,1,-9]
#k=5
# 8
#print(f(pnl,k))

def helper(pnl,k):
  n = len(pnl)
  window = 0
  res = 0
  for i in range(0,n):
    window += pnl[i]
    if i >=k:
      window -= pnl[i-k]
    if i >= k-1:
      res = max(res,window)
  return res

def getMaxProfit(pnl,k):
  res = 0
  for i in range(1,k+1):
    res = max(res,helper(pnl,i))
  return res

def longestsubarrayatmostk(arr, k):
    neg = []
    S = 0
    for i in range(len(arr)-1,-1,-1):
        neg.append(S)
        S += arr[i]
        S = min(0, S)
    neg = neg[::-1]
  
    S = 0
    i, j = 0, 0
    res = 0
    while j < len(arr):
        S += arr[j]
        while i < len(arr) and neg[j] + S > k:
            S -= arr[i]
            i += 1
        res = max(res, j - i + 1)
        j += 1
    return res
pnl = [-3,4,3,-2,2,5]
k = 4
print(longestsubarrayatmostk(pnl,k))

"""
SELECT DISTINCT SUM(
         COALESCE(SUM(t.Amount), 0) -
         CASE 
           WHEN SUM((t.Amount < 0)::int) < 3 OR SUM(CASE WHEN t.Amount < 0 THEN -t.Amount ELSE 0 END) < 100 THEN 5
           WHEN SUM((t.Amount < 0)::int) in (3,4,5) AND SUM(CASE WHEN t.Amount < 0 THEN -t.Amount ELSE 0 END) > 100 THEN 3 
           ELSE 0  
         END
       ) OVER () total
FROM generate_series(1, 12, 1) m(month) LEFT JOIN transactions t 
ON m.month = date_part('month', t.dt) AND date_part('year', t.dt) = 2020
GROUP BY m.month
"""