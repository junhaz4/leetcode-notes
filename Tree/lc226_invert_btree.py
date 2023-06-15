# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree_recursion(self, root):
        '''
        Use dfs recursion method. Could use either preorder and postorder but not inorder
        because inorder
        First swap left and right child. Then recursive call on left child and right child 
        '''
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree_recursion(root.left)
        self.invertTree_recursion(root.right)
        return root
    
    def invertTree_stack(self,root):
        '''
        Use dfs stack method. 
        '''
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            # postorder 
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            # preorder
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root
    
    def invertTree_queue(self,root):
        '''
        use bfs queue method
        '''
        if not root:
            return root
        from collections import deque
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                node.left, node.right = node.right,node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        