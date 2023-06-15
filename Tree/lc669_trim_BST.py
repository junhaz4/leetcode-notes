 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            # 若当前root节点小于左界：只考虑其右子树，用于替代更新后的其本身，抛弃其左子树整体
            return self.trimBST(root.right,low,high)
        if root.val > high:
            # 若当前root节点大于右界：只考虑其左子树，用于替代更新后的其本身，抛弃其右子树整体
            return self.trimBST(root.left,low,high)
       
        root.left = self.trimBST(root.left,low,high) #root->left接入符合条件的左孩子
        root.right = self.trimBST(root.right,low,high) #root->right接入符合条件的右孩子
        return root

# method 2
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        #处理头结点，让root移动到[L, R] 范围内，注意是左闭右闭
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            else:
                root = root.left
        #此时root已经在[L, R] 范围内，处理左孩子元素小于L的情况
        cur = root
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left
            
        #此时root已经在[L, R] 范围内，处理右孩子大于R的情况
        cur = root
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        return root