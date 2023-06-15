class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums):
        '''Method 1'''
        # if nums is empty
        if not nums:
            return None
        # find the max in nums and its index
        val = max(nums)
        index = nums.index(val)
        root = TreeNode(val)
        # seperate nums into 2 sub-lists
        left = nums[:index]
        right = nums[index+1:]
        # recursively construct left and right subtree
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root
    
        '''Method 2'''
        def traversal(nums,begin,end):
            if begin == end:
                return None
            # find maximum index
            index = begin
            for i in range(begin,end):
                if nums[i]>nums[index]:
                    index = i
            root = TreeNode(nums[index])
            # recursively construct left and right subtree
            root.left =  traversal(nums,begin,index)
            root.right = traversal(nums,index+1,end)
        return traversal(nums,0,len(nums))