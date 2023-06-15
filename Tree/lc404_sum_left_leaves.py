# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves_recursion(self, root) -> int:
        def getSum(node):
            if not node:
                return 0
            left = getSum(node.left)
            right = getSum(node.right)
            total = 0
            if node.left and not node.left.left and not node.left.right:
                total += node.left.val
            return total + left + right
        return getSum(root)
    
    def sumOfLeftLeaves_stack(self, root):
        if not root:
            return 0
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                result += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result 