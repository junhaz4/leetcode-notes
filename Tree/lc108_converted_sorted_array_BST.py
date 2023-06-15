class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def traversal(nums,left,right):
            # base case 
            if left > right:
                return None
            # 确定左右界的中心，防越界
            mid = left + (right-left)//2
            # 构建根节点
            node = TreeNode(nums[mid])
            # 构建以左右界的中心为分割点的左右子树
            node.left = traversal(nums,left,mid-1)
            node.right = traversal(nums, mid+1, right)
            return node
        root = traversal(nums,0,len(nums)-1)
        return root