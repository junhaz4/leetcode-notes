# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth_queue(self, root):
        '''
        bfs level order traversal. The max depth is equal to the number of order traversal
        or could also store a count and increment every time we traversl each level
        '''
        if not root:
            return 0
        queue = [root]
        count = 0
        while queue:
            size = len(queue)
            count += 1
            for _ in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return count
        
        
        if root == None:
            return 0
        queue_ = [root]
        result = []
        while queue_:
            length = len(queue_)
            sub = []
            for i in range(length):
                cur = queue_.pop(0)
                sub.append(cur.val)
                if cur.left: 
                    queue_.append(cur.left)
                if cur.right: 
                    queue_.append(cur.right)
            result.append(sub)
        return len(result)
    
    def maxDepth_recursion(self, root):
        '''
        use recursion to count the depth
        preorder finds the maximum depth of tree and postorder finds the maximum height of root 
        max depth of tree is max height of root, so either preorder or postorder works 
        '''
        if not root:
            return 0
        def get_depth(node):
            if not node:
                return 0
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            depth = 1+max(left_depth,right_depth)
            return depth
        return get_depth(root)