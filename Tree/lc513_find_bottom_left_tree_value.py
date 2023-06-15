# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue_queue(self, root) -> int:
        '''
        bfs leverl order traversal, return the first element in the last level
        '''
        from collections import deque
        results = []
        queue = deque([root])
        while queue:
            size = len(queue)
            result = []
            for _ in range(size):
                node = queue.popleft()
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(result)
        return results[-1][0]
        
        # more easy way is to traversal from right to left and the last element will be the leftmost leaf in the tree
        queue = [root]
        while queue:
            node = queue.pop(0)
            result = node.val
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return result
        
        # can also use a depth to indicate the leaf node because the leaf node has the largest depth
        # because we are finding the leftmost leaf node, so need traversal from left to right, the first element 
        # having the largest depht will be the answer
        queue = deque([[root,1]])
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            if depth>max_depth:
                max_depth = depth
                result = node.val
            if node.left:
                queue.append([node.left, depth+1])
            if node.right:
                queue.append([node.right, depth+1])
        return result
        