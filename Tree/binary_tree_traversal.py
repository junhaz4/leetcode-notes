'''
Two types of traversal for binary tree

DFS VS BFS

DFS: 
1. Preorder traversal: root left right
2. Inorder traversal: left root right
3. postorder traversal: left right root
Note: Postorder can be obtained by modify preorder
reverse(root right left) -> left right root

BFS:
level order traversal: level by level from top to bottom

'''
# Leetcode 144, 94, 145, 102

class TreeNode:
    def __inint__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
   
        
####################################################################################################################
# Preorder Traversal

## Recursion
def preorderRecurisonl(root):
    result = []
    def traversal(node):
        if not node:
            return 
        result.append(node.val)
        traversal(node.left)
        traversal(node.right)
    traversal(root)
    return result
    
## Stack    
def preorderStack(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        # middle node out stack in result 
        node = stack.pop()
        result.append(node.val)
        # right node in stack
        if node.right:
            stack.append(node.right)
        # left node in stack
        if node.left:
            stack.append(node.left)
    return result


####################################################################################################################
# Inorder Traversal

## Recursion
def inorderRecurisonl(root):
    result = []
    def traversal(node):
        if not node:
            return 
        traversal(node.left)
        result.append(node.val)
        traversal(node.right)
    traversal(root)
    return result 

## Stack
def inorderStack(root):
    if not root:
        return []
    result = []
    stack = []
    cur = root
    while cur or stack:
        # recursion to the bottom left node then in stack
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            # left node out stack
            # middle node out stack
            # right node out stack
            cur = stack.pop()
            result.append(cur.val)
            cur= cur.right
    return result
            
###################################################################################################################
# Postorder Traversal

## Recursion
def postorderRecurisonl(root): 
    result = []
    def traversal(node):
        if not root:
            return 
        traversal(node.left)
        traversal(node.right)
        result.append(node.val)
    traversal(root)
    return result
        
## Stack
def postorderStack(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]


###################################################################################################################
# Level Order Traversal

## Recursion
def levelorderRecursion(root):
    result = []
    def traversal(node,depth):
        if not node:
            return []
        # start from the current depth
        if len(result)==depth:
            result.append([])
        # fulfill the node in current depth
        result[depth].append(node.val)
        # process the left node 
        if node.left:
            traversal(node.left,depth+1)
        # process the right node
        if node.right:
            traversal(node.right,depth+1)
    traversal(root,0)
    return result

## Queue   
from collections import deque
def levelorderQueue(root):
    results = []
    if not root:
        return []
    que = deque([root])
    while que:
        size = len(que)
        result = []
        # node in the same depth out stack into result
        for _ in range(size):
            node = que.popleft()
            result.append(node.val)
            # left node into queue
            if node.left:
                que.append(node.left)
            # right ndoe into queue    
            if node.right:
                que.append(node.right)
        results.append(result)
    return results


