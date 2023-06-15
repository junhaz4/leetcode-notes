# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Depth: the total number of edges from root node to target node
To solve depth related problems, we need to check from top to down using preorder
Height: the longest simple path from root node to leaf node 
To solve height related problems, we need to check from bottom to top using postorder.

Three step to determine the recursion
1. Figure out the parameter and return value 
parameter: the current node
return: the height of tree with current node as root
2. Figure out the stop 
If we encounter empty node, then return 0 meaning that the height of tree with current node as root is 0
3. Determine recursion rule
To check the tree with current node as root is balanced, compute the height of left subtree and right subtree and 
if the difference is less than 1, then return the height of current tree, else return -1 to mark inbalanced tree
'''
class Solution:
    def isBalanced(self, root):
        '''
        To check the height of a tree, we need to check it from bottom to top. 
        Use recursion to check the height of left subtree of right subtree
        Use -1 to denote subtree is not balanced or the differ is greater than 1
        '''
        def getHeight(node):
            if not node:
                return 0
            left = getHeight(node.left)
            right = getHeight(node.right)
            if left == -1:
                return -1
            if right == -1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        if getHeight(root)!= -1:
            return True
        return False
        
        def height(node):
            if not node:
                return 0,True
            l, l_balance = height(node.left)
            r, r_balance = height(node.rright)
            if not l_balance or not r_balance:
                return 0, False
            if abs(l-r)>1:
                return 0, False
            return 1+max(l,r), True
        return height(root)[1]
