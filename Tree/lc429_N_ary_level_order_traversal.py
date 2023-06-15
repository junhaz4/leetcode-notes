
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
class Solution:
    def levelOrder(self, root: 'Node'):
        '''
        Use bfs level order traversal
        node.children is a list so need use extend not append 
        '''
        from collections import deque
        if not root:
            return []
        results = []
        queue = deque([root])
        while queue:
            result = []
            for _ in range(len(queue)):
                node = queue.popleft()
                result.append(node.val)
                if node.children:
                    queue.extend(node.children)
            results.append(result)
        return results


a = Solution
a.levelOrder()