class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        # Method 1 -> recursion to store all nodes into a list 
        '''
        The inorder traversal of bst gives a strictly increasing list, so can use it to check
        '''
        result = []
        def traversal(node):
            if not node:
                return 
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)
        traversal(root)
        for i in range(1,len(result)):
            if result[i] >= result[i-1]:
                return False
        return True
    
    
        # Method 2
        maxValue = -float('inf')
        def isvalid(root):
            if not root:
                return True 
            left = isvalid(root.left)
            if maxValue < root.val:
                maxValue = root.val
            else:
                return False 
            right = isvalid(root.right)
            return left and right 
        return isvalid(root)
    
    
        # Method 3 Iteration
        stack = []
        cur = root
        pre = None 
        while cur or stack:
            # point to the bottom left node
            if cur:
                stack.append(cur)
                cur= cur.left
            else:
                cur = stack.pop()
                # compare the value of current and its previous node
                if pre and cur.val <= pre.val:
                    return False
                pre = cur
                cur = cur.right
        return True