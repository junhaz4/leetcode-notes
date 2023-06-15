class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 返回更新后的以当前root为根节点的新树，方便用于更新上一层的父子节点关系链

        # Base Case
        if not root: return TreeNode(val)

        # 单层递归逻辑:
        if val < root.val: 
            # 将val插入至当前root的左子树中合适的位置
            # 并更新当前root的左子树为包含目标val的新左子树
            root.left = self.insertIntoBST(root.left, val)

        if root.val < val:
            # 将val插入至当前root的右子树中合适的位置
            # 并更新当前root的右子树为包含目标val的新右子树
            root.right = self.insertIntoBST(root.right, val)

        # 返回更新后的以当前root为根节点的新树
        return root

# method 2
def insertIntoBST(self, root, val: int):
    newNode = TreeNode(val)
    if not root: return newNode
    
    if not root.left and val < root.val:
        root.left = newNode
    if not root.right and val > root.val:
        root.right = newNode
    
    if val < root.val:
        self.insertIntoBST(root.left, val)
    if val > root.val:
        self.insertIntoBST(root.right, val)
    
    return root

# method 3
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: 
            return TreeNode(val)
        parent = None
        cur = root

        # 用while循环不断地找新节点的parent
        while cur: 
            if cur.val < val: 
                parent = cur
                cur = cur.right
            elif cur.val > val: 
                parent = cur
                cur = cur.left

        # 运行到这意味着已经跳出上面的while循环, 
        # 同时意味着新节点的parent已经被找到.
        # parent已被找到, 新节点已经ready. 把两个节点黏在一起就好了. 
        if parent.val > val: 
            parent.left = TreeNode(val)
        else: 
            parent.right = TreeNode(val)
        
        return root
