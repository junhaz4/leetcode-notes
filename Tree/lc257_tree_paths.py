# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths_recursion(self, root):
        '''
        The backtraking part is shown in the recursive call path+'->' because the current path does not add '->'
        '''
        result = []
        path = ""
        # node is the current node and path is the path from root to the current node
        def getPath(node,path):
            path += str(node.val)
            # leaf node and append the path to result 
            if not node.left and not node.right:
                result.append(path)
            # keeping finding path along left child
            if node.left:
                getPath(node.left, path+'->')
            # keeping find path along right child 
            if node.right:
                getPath(node.right, path+'->')
        getPath(root, path)
        return result
    
    def binaryTreePaths_backtrack(self,root):
        '''
        A more explicit backtracking function
        '''
        result = []
        paths = []
        def getPath(node,path):
            path.append(node.val)
            # reach to leaf node, modify the path into required form
            if not node.left and not node.right:
                spath =""
                for i in range(len(path)-1):
                    spath+=str(path[i])
                    spath += '->'
                spath += str(path[len(path)-1])
                result.append(spath)
                return
            if node.left:
                getPath(node.left, path)
                path.pop()  # backtracking to pop the last in path
            if node.right:
                getPath(node.right,path)
                path.pop()

        getPath(root,paths)
        return result

    
    def binaryTreePaths_stack(self, root):
        '''
        To find all path from root to lead node, we use dfs preorder traversal with stack
        and an extra list to store the path and root containing at least one node
        '''
        stack = [root]
        paths = [str(root.val)]
        result = []
        while stack:
            cur = stack.pop()
            path = paths.pop()
            # if reach to a leaf node, then put path in result
            if not cur.left and not cur.right:
                result.append(path)
            # either left first or right first is the same
            if cur.left:
                stack.append(cur.left)
                paths.append(path+'->'+cur.left.val)
            if cur.right:
                stack.append(cur.right)
                paths.append(path+'->'+cur.right.val)
        return result
    
    def binaryTreePaths_queue(self, root):
        '''
        Similarly we can use queue
        '''
        result = []
        from collections import deque
        queue = deque([root])
        paths = deque([str(root.val)])
        while queue:
            cur = queue.popleft()
            path = paths.popleft()
            if not cur.left and not cur.right:
                result.append(path)
            if cur.left:
                queue.append(cur.left)
                paths.append(path+'->'+str(cur.left.val))
            if cur.right:
                queue.append(cur.right)
                paths.append(path +'->'+str(cur.right.val))
        return result