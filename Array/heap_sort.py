def heap_sort(nums):
  def max_heapify(size,index):
    largest = index
    left, right = 2*index+1, 2*index+2
    if left < size and nums[left] > nums[largest]:
      largest = left
    if right < size and nums[right] > nums[largest]:
      largest = right
    if largest != index:
      nums[largest], nums[index] = nums[index], nums[largest]
      max_heapify(size, largest)
    
  n = len(nums)
  # heapify the original list
  for i in range(n//2 -1, -1, -1):
    max_heapify(n,i)
  for i in range(n-1, 0, -1):
    nums[0], nums[i] = nums[i], nums[0]
    max_heapify(i,0)
  
  # time complexity: O(nlogn)
  # space complexity: O(1)