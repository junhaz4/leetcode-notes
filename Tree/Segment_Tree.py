class SegmentTreeNode:
  def __init__(self, start, end, val, left=None, right=None):
    self.start = start
    self.end = end
    self.mid = start + (end - start) // 2
    self.val = val
    self.left = left
    self.right = right
 
class NumArray:
  def __init__(self, nums):
    self.nums = nums
    if self.nums:
      self.root = self._buildTree(0, len(nums) - 1)
 
  def update(self, i, val):      
    self._updateTree(self.root, i, val)
 
  def sumRange(self, i, j):
    return self._sumRange(self.root, i, j)
    
  def _buildTree(self, start, end):
    if start == end: return SegmentTreeNode(start, end, self.nums[start])
    mid = start + (end - start) // 2
    left = self._buildTree(start, mid)
    right = self._buildTree(mid + 1, end)
    return SegmentTreeNode(start, end, left.val + right.val, left, right)
  
  def _updateTree(self, root, i, val):
    if root.start == i and root.end == i:
      root.val = val
      return    
    if i <= root.mid:
      self._updateTree(root.left, i, val)
    else:
      self._updateTree(root.right, i, val)
    root.val = root.left.val + root.right.val
  
  def _sumRange(self, root, i, j):
    if root.start == i and root.end == j:
      return root.val
    if j <= root.mid:
      return self._sumRange(root.left, i, j)
    elif i > root.mid:
      return self._sumRange(root.right, i, j)
    else:
      return self._sumRange(root.left, i, root.mid) + self._sumRange(root.right, root.mid + 1, j)
    
# https://zxi.mytechroad.com/blog/sp/segment-tree-sp14/ 
# build: O(n)
# update: O(logn)
# rangeQuery: O(logn+k)