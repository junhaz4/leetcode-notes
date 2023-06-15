# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Method 1 Recursion
        # p and q are both in the right side
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        # p and q are both in the left side
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        # p and q in different side and the root is the solution
        else:
            return root   
        
         
        # Method 2 Iteration 
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root          
           
        # Method 3
        '''
        To search the lowest common ancestor, need to search it from bottom to top and postorder traversal can achieve this 
        从跟节点开始，左树和右树开始。从叶子节点开始往上逐层搜索。需要recursion搜素整棵树，递归函数返回值是node，使用left 和 right将返回值存起来，
        left和right后续还要进行逻辑处理
        '''
        # 如果节点到了p，q或者遇到空节点，返回该节点
        if root==p or root==q or root==None:
            return root
        # 左边和右边搜索的结果存起来
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 左右搜索都有结果，那说明当前root是最小祖宗
        if left and right:
            return root
        # 右无结果，说明在左边，返回左边的结果
        elif left and not right:
            return left
        # 左边无结果，说明在右边，返回右边的值
        elif not left and right:
            return right
        else:
            return None
        