# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root, targetSum) -> bool:
        # Recursion1
        if not root:
            return False 
        # first check leaf node, the subtract node val from targetsum
        if not root.left and not root.right:
            return root.val == targetSum
        
        # could also subtract first and then check the leaf node val is 0 or not 
        newSum = targetSum-root.val
        if not root.left and not root.right:
            return newSum == 0
              
        return (self.hasPathSum(root.left, newSum)) or (self.hasPathSum(root.right,newSum))
    
        # Recursion 2
    def hashpathsum(self,root,targetSum):
        def dfs(node,cursum):
            if not node.left and not node.right:
                return cursum==0
            if node.left:
                cursum -= node.left.val
                if dfs(node.left, cursum):
                    return True
                cursum += node.left.val
            if node.right:
                cursum -= node.right.val
                if dfs(node.right, cursum):
                    return True
                cursum += node.right.val
            return False
        return dfs(root,targetSum-root.val)
        
        # Queue
    def hashPathsum(self,root,targetSum):
        if root==[]:
            return 0
        result = []
        paths = []
        
        def getPath(node,path):
            if not node:
                return 0
            path.append(node.val)
            # reach to leaf node, modify the path into required form
            if not node.left and not node.right:
                result.append(sum(path))
                return 
            if node.left:
                getPath(node.left, path)
                path.pop()  # backtracking to pop the last in path 
            if node.right:
                getPath(node.right,path)
                path.pop()
        getPath(root,paths)
        for p in result:
            if p==targetSum:
                return True
        return False 
        