class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
"""
第一种情况：没找到删除的节点，遍历到空节点直接返回了
找到删除的节点
第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
第三种情况：删除节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
第四种情况：删除节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
第五种情况：左右孩子节点都不为空，则将删除节点的左子树头结点（左孩子）放到删除节点的右子树的最左面节点的左孩子上，返回删除节点右孩子为新的根节点。
"""
class Solution:
    def deleteNode(self, root: TreeNode, key: int):
        # 第一种情况：没找到删除的节点，遍历到空节点直接返回了
        if not root:
            return None
        if root.val < key :
            root.right = self.deleteNode(root.right, key)
        elif root.val > key :
            root.left = self.deleteNode(root.left, key)
        # 找到了要删除的节点，根据以下情况处理
        else:
            # 第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
            if not root.left and not root.right:
                return None
            # 第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
            elif root.left and not root.right:
                return root.left
            #第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
            elif not root.left and root.right:
                return root.right
            #第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置并返回删除节点右孩子为新的根节点。
            else:
                temp = root.right
                while temp.left:
                    temp = temp.left
                temp.left = root.left
                root = root.right
        return root
