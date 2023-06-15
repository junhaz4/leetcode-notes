# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root) -> int:
        # Method 1 store all nodes into a list and compare the difference
        result = []
        minValue = float('inf')
        def traversal(node):
            if not node:
                return 
            traversal(node.left)
            result.append(node.val)
            traversal(node.right)
        traversal(root)
        for i in range(len(result)-1):
            minValue = min(abs(result[i]-result[i+1]),minValue)
        return minValue
    
        # Method 2 use a pointer to store previous node
        prev = None 
        result = float('inf')
        def traversal2(node):
            nonlocal prev, result
            if not node:
                return 
            traversal2(node.left)
            if prev:
                result = min(abs(node.val-prev.val),result)
            prev = node
            traversal2(node.right)
        traversal(root)
        return result 
    
    
        # Method 3 Iteration using stack
        stack = []
        cur = root
        pre = None
        result = float('inf')
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                if pre: # 当前节点和前节点的值的差值
                    result = min(result, cur.val - pre.val)
                pre = cur
                cur = cur.right
        return result
        
            