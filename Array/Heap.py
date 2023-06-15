class MinHeap:
  def __init__(self, data=None):  # construct heap from an array
    self.data = list(data) if data else []
    for i in range((len(self.data)) // 2, -1, -1): # start from the second last level to the top level
      self.heapifyDown(i)
  
  def push(self, key):
    self.data.append(key)
    self.heapifyUp(len(self.data) - 1)
 
  def pop(self):
    self.swap(0, -1)
    min_el = self.data.pop()
    self.heapifyDown(0)
    return min_el
  
  def size(self):
    return len(self.data)
  
  def swap(self, i, j):
    self.data[i], self.data[j] = self.data[j], self.data[i]
    
  def heapifyDown(self, i):
    smallest = i
    for c in [2 * i + 1, 2 * i + 2]: # c represents the index of children
      if c < self.size() and self.data[c] < self.data[smallest]:
        smallest = c
    if smallest != i:  # not reach to the end. If smallest==i => no child and reach to end 
      self.swap(i, smallest)
      self.heapifyDown(smallest)
  
  def heapifyUp(self, i):
    if i == 0: 
      return
    parent = (i - 1) // 2
    if self.data[i] >= self.data[parent]:  # don't swap if parent is less than children
      return
    self.swap(i, parent)
    self.heapifyUp(parent)
    

# heap method       time complexity   space complexity:
# Construct a Heap   O(N)                 O(N)
# insert             O(logN)              O(1)
# delete             O(logN)              O(1)
# get the top element O(1)                O(1)
# get the size of heap O(1)               O(1)