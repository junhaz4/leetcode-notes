# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes_queue(self, root):
        '''
        bfs leverl order traversal using queue
        '''
        if not root:
            return 0
        result = 0
        from collections import deque
        queue = deque([root])
        while queue:
            size = len(queue)
            result += size
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    def countNodes_stack(self, root):
        '''
        use dfs preorder traversal.increment the count every time pop element
        '''
        if not root:
            return 0
        count = 0
        stack = [root]
        while stack:
            node = stack.pop()
            count +=1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return count 
    
    def countNodes_recursion(self, root):
        '''
        use recursion on postorder traversal
        '''
        def getNum(node):
            if not node:
                return 0
            left = getNum(node.left)
            right = getNum(node.right)
            return left+right+1
        return getNum(root)