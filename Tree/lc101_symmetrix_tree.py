# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric_recursion(self, root):
        '''
        Use recursion to compare the left subtree and right subtree
        For left subtree, the traversal order is left right middle
        For right subtree, the traversal order is right left middle
        Compare the outer node, compare the inner node. 
        '''
        def traversal(left,right):
            # right child is empty
            if left != None and right==None:
                return False
            # left child is empty 
            elif left == None and right != None:
                return False
            # both empty 
            elif left == None and right == None:
                return True
            # both not empty and val not equal  
            elif left.val != right.val:
                return False
            # val equal and check subtree
            else:
                return traversal(left.left, right.right) and traversal(left.right, right.left)
        
        if not root:
            return True
        return traversal(root.left,root.right)
    
    def isSymmetric_queue(self, root):
        '''
        use stack each time put the symmetric left and right node into queue and compare them
        keeping putting outer nodesand inner nodes into queue
        '''
        from collections import deque 
        if not root:
            return True 
        queue = deque([root.left,root.right])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True