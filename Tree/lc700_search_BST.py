# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root, val):
        
        # Method 1 Recursion
        '''
        Binary search tree has order. All node to the left of root is less than root and all right node is larger than root
        So we use the order of BST to check is certain value exists.
        '''
        # if root is empty or we find the val
        if not root or root.val == val:
            return root
        # search the right subtree
        if root.val < val:
            return self.searchBST(root.right, val)
        # search the left subtree
        if root.val > val:
            return self.searchBST(root.left, val)
        return None
    
    
        # Method 2 Iteration
        '''
        Because of the natural order of bst, we dont need to use stack or queue for iteration since the order helps decide the search direction
        '''
        if not root:
            return None
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
            return None