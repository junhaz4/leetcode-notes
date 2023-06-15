# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return []
        result = []
        path = []
        dfs(root,targetSum,path)
        return result 
    
        def dfs(node,curSum,curPath):
            if not node:
                return
            # method 1
            curPath.append(node.val)
            curSum -= node.val
            if not node.left and not node.right:
                if curSum == 0:
                    result.append(curPath[:])
            else:
                dfs(node.left,curSum,curPath)
                dfs(node.right,curSum,curPath)
            curPath.pop()
            
            # method 2
            curPath.append(node.val)
            if not node.left and not node.right:
                if curSum == node.val:
                    result.append(curPath[:])
            else:
                curSum -= node.val
                dfs(node.left,curSum,curPath)
                dfs(node.right,curSum,curPath)
            curPath.pop()
        
        # method 3
        result = []
        path = [root]
        def traversal(node,curSum):
            if not node.left and not node.right and curSum == 0:
                result.append(path[:])
                return 
            if not node.left and not node.right:
                return 
            if node.left:
                path.append(node.left.val)
                curSum -= node.left.val
                traversal(node.left,curSum)
                curSum += node.left.val
                path.pop()
            if node.right:
                path.append(node.right.val)
                curSum -= node.right.val
                traversal(node.right,curSum)
                curSum += node.right.val
                path.pop()
        traversal(root,targetSum-root.val)
        return result
    