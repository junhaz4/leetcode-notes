import collections


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def deepestLeavesSum(self, root):
        # BFS Level order traversal
        if not root:
            return 0
        que = collections.deque([root])
        level_sum = 0
        while que:
            size = len(que)
            level_sum = 0
            for _ in range(size):
                cur = que.popleft()
                level_sum += cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)

        #return level_sum

        # DFS
        if not root:
            return 0
        depth, dpt_sum = 0,0
        stack = [(root,0)]
        while stack:
            node, cur_depth = stack.pop()
            # check if the node is a leaf node
            if node.left is None and node.right is None:
                if depth < cur_depth:
                    depth = cur_depth
                    dpt_sum = node.val
                elif depth == cur_depth:
                    dpt_sum += node.val
            else:
                if node.right:
                    stack.append([node.right,cur_depth+1])
                if node.left:
                    stack.append([node.left,cur_depth+1])

        return dpt_sum


