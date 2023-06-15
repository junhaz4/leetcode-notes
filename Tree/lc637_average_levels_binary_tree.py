# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root):
        '''
        The idea is to use bfs level order traversal. Add the value in each level and divide by queue siez
        '''
        from collections import deque
        if not root:
            return []
        result = []
        queue =deque([root])
        while queue:
            size = len(queue)
            total = 0
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(total/size)
        return result

#[3,9,20,null,null,15,7]
#[3,9,20,15,7]