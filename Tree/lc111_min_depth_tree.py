# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # BFS Method
    def minDepth_bfs(self, root):
        '''
        The idea is to use bfs level order traversal. The element in queue is a pair consisting the node and depth
        If a node doesn't have left and right child, then the current depth is the min depth from the root
        Note: When initializing the queue, if the element in queue is not single, need to use braket to put them together
        because queue=deque([]) is a list[]
        '''
        from collections import deque
        if not root:
            return 0
        queue = deque([[root,1]])
        while queue:
            node,depth = queue.popleft()
            if node.left==None and node.right==None:
                return depth
            if node.left:
                queue.append([node.left,depth+1])
            if node.right:
                queue.append([node.right,depth+1])
        return 0

    # DFS Method
    def minDepth_dfs(self, root):
        '''
        The idea is to use dfs stack. The element in stack is also a pair containing the node and the depth
        One thing to note is that need to pop(0) the first element in stack instead of the last one.
        If the node without children is on the left side, if we pop the last element in the stack(right node), then
        the children of the right node will be put in the stack after the left node
        and those children node will be explore first and return the wrong depth when reaching to the their leaf node, 
        so need to pop the first element.
        '''
        if not root:
            return 0
        stack=[(root,1)]
        while stack:
            node,depth = stack.pop(0)
            if node.left==None and node.right==None:
                return depth
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
        return 0