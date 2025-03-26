class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    memo = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        # 每个节点都有2个状态，选或者不选
        # 记忆化递归
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val 
        if root in self.memo:
            return self.memo[root]
        res1 = root.val 
        if root.left:
            res1 += self.rob(root.left.left)+self.rob(root.left.right)
        if root.right:
            res1 += self.rob(root.right.left)+self.rob(root.right.right)
        res2 = self.rob(root.left)+self.rob(root.right)
        self.memo[root] = max(res1,res2)
        return max(res1,res2)
    
class Solution:
    memo = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        # 每个节点都有2个状态，选或者不选
        # 动态规划
        # dp长度为2，记录不偷节点和偷节点的金额

        def dfs(node):
            if not node:
                return 0,0
            left_not_rob, left_rob = dfs(node.left)
            right_not_rob, right_rob = dfs(node.right)
            # 偷中间节点，左右孩子节点不能偷
            res1 = node.val + left_not_rob + right_not_rob
            # 不偷中间节点，左右孩子可以偷，选一个最大的
            res2 = max(left_not_rob,left_rob)+max(right_not_rob,right_rob)
            return res2,res1
        return max(dfs(root))