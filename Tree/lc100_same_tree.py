# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree_queue(self, p, q) -> bool:
        '''
        use queue to compare the node the same position in each tree
        '''
        from collections import deque
        queue = deque([p,q])
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.left)
            queue.append(node1.right)
            queue.append(node2.right)
        return True
    
    def isSameTree_recursion(self,p,q):
        '''
        use recursion to compare each node 
        '''
        def compare(t1,t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False
            elif t1.val != t2.val:
                return False
            return compare(t1.left, t2.left) and compare(t1.right,t2.right)
        return compare(p,q)