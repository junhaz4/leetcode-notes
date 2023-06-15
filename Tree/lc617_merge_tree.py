 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def mergeTrees(self, root1, root2) ->[TreeNode]:
        '''
        use queue to store node at the same postion if both node exists
        '''
        # Method 1 Deque
        if not root1:
            return root2
        if not root2:
            return root1
        from collections import deque 
        queue = deque([root1,root2])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            # only append if both have left child 
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            # only append if both have right child 
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
            node1.val += node2.val
            # if node1 has no left but node2 has, then update node1.left
            if not node1.left and node2.left:
                node1.left = node2.left
            # if node1 has no right but node2 has, then update node1.right
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1
        
        # Method 2 Recursion 
        #  if one node is empty, return the other
        if not root1: 
            return root2
        if not root2: 
            return root1
        # the above conditions make sure that both root1 and root2 are non-empty when run the following steps
        root1.val += root2.val # 中
        root1.left = self.mergeTrees(root1.left, root2.left) #左
        root1.right = self.mergeTrees(root1.right, root2.right) # 右
        return root1    