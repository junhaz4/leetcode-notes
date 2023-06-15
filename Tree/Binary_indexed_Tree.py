class  FenwickTree:
  def __init__(self, n):
    self._sums = [0 for _ in range(n + 1)]
    
  def update(self,i,value):
    while i < len(self._sums):
      self._sums[i] += value
      i += i & -i
      
  def query(self,i):
    s = 0
    while i > 0:
      s += self._sums[i]
      i -= i & -i
    return s
  
# Init the tree (include building all prefix sums) takes O(nlogn)
# Update the value of an element takes O(logn)
# Query the range sum takes O(logn)
# Space complexity: O(n)
      