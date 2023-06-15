# lc 199

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left         
        self.right = right
        
class Solution:
    def rightSideView(self, root):
        '''
        Idea: 
        1. Use bfs level order traversal to get nodes in each level and put into queue
        2. The last element in queue is the node on the right tree in each level
        '''
        if not root:
            return []
        from collections import deque 
        queue= deque([root])
        result = []
        while queue:
            # last node is the on the right side in every level
            node = queue[-1]
            result.append(node.val)
            # get all the node in the next level
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
 
