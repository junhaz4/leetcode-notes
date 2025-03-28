"""AVL 树既是二叉搜索树，也是平衡二叉树，同时满足这两类二叉树的所有性质，因此是一种平衡二叉搜索树（balanced binary search tree）。"""
class TreeNode:
    """AVL 树节点类"""
    def __init__(self, val: int): 
      self.val: int = val                 # 节点值
      self.height: int = 0                # 节点高度
      self.left: TreeNode | None = None   # 左子节点引用
      self.right: TreeNode | None = None  # 右子节点引用
    
  def height(self, node: TreeNode | None) -> int:
      """获取节点高度"""
      # 空节点高度为 -1 ，叶节点高度为 0
      if node is not None:
          return node.height
      return -1
  
  def update_height(self, node: TreeNode | None):
      """更新节点高度"""
      # 节点高度等于最高子树高度 + 1
      node.height = max([self.height(node.left), self.height(node.right)]) + 1

  def balance_factor(self, node: TreeNode | None) -> int:
      """获取平衡因子"""
      # 空节点平衡因子为 0
      if node is None:
          return 0
      # 节点平衡因子 = 左子树高度 - 右子树高度
      return self.height(node.left) - self.height(node.right)


"""
AVL 树的特点在于“旋转”操作，它能够在不影响二叉树的中序遍历序列的前提下，使失衡节点重新恢复平衡。换句话说，旋转操作既能保持“二叉搜索树”的性质，也能使树重新变为“平衡二叉树”。
我们将平衡因子绝对值的节点称为“失衡节点”。根据节点失衡情况的不同，旋转操作分为四种：右旋、左旋、先右旋后左旋、先左旋后右旋
"""

  def right_rotate(self, node: TreeNode | None) -> TreeNode | None:
      """右旋操作"""
      child = node.left
      grand_child = child.right
      # 以 child 为原点，将 node 向右旋转
      child.right = node
      node.left = grand_child
      # 更新节点高度
      self.update_height(node)
      self.update_height(child)
      # 返回旋转后子树的根节点
      return child

"""右旋和左旋操作在逻辑上是镜像对称的，它们分别解决的两种失衡情况也是对称的。基于对称性，我们只需将右旋的实现代码中的所有的 left 替换为 right ，将所有的 right 替换为 left"""
  def left_rotate(self, node: TreeNode | None) -> TreeNode | None:
      """左旋操作"""
      child = node.right
      grand_child = child.left
      # 以 child 为原点，将 node 向左旋转
      child.left = node
      node.right = grand_child
      # 更新节点高度
      self.update_height(node)
      self.update_height(child)
      # 返回旋转后子树的根节点
      return child

  def rotate(self, node: TreeNode | None) -> TreeNode | None:
      """执行旋转操作，使该子树重新恢复平衡"""
      # 获取节点 node 的平衡因子
      balance_factor = self.balance_factor(node)
      # 左偏树
      if balance_factor > 1:
          if self.balance_factor(node.left) >= 0:
              # 右旋
              return self.right_rotate(node)
          else:
              # 先左旋后右旋
              node.left = self.left_rotate(node.left)
              return self.right_rotate(node)
      # 右偏树
      elif balance_factor < -1:
          if self.balance_factor(node.right) <= 0:
              # 左旋
              return self.left_rotate(node)
          else:
              # 先右旋后左旋
              node.right = self.right_rotate(node.right)
              return self.left_rotate(node)
      # 平衡树，无须旋转，直接返回
      return node

  def insert(self, val):
      """插入节点"""
      self._root = self.insert_helper(self._root, val)
  
  def insert_helper(self, node: TreeNode | None, val: int) -> TreeNode:
      """递归插入节点（辅助方法）"""
      if node is None:
          return TreeNode(val)
      # 1. 查找插入位置并插入节点
      if val < node.val:
          node.left = self.insert_helper(node.left, val)
      elif val > node.val:
          node.right = self.insert_helper(node.right, val)
      else:
          # 重复节点不插入，直接返回
          return node
      # 更新节点高度
      self.update_height(node)
      # 2. 执行旋转操作，使该子树重新恢复平衡
      return self.rotate(node)


  def remove(self, val: int):
      """删除节点"""
      self._root = self.remove_helper(self._root, val)
  
  def remove_helper(self, node: TreeNode | None, val: int) -> TreeNode | None:
      """递归删除节点（辅助方法）"""
      if node is None:
          return None
      # 1. 查找节点并删除
      if val < node.val:
          node.left = self.remove_helper(node.left, val)
      elif val > node.val:
          node.right = self.remove_helper(node.right, val)
      else:
          if node.left is None or node.right is None:
              child = node.left or node.right
              # 子节点数量 = 0 ，直接删除 node 并返回
              if child is None:
                  return None
              # 子节点数量 = 1 ，直接删除 node
              else:
                  node = child
          else:
              # 子节点数量 = 2 ，则将中序遍历的下个节点删除，并用该节点替换当前节点
              temp = node.right
              while temp.left is not None:
                  temp = temp.left
              node.right = self.remove_helper(node.right, temp.val)
              node.val = temp.val
      # 更新节点高度
      self.update_height(node)
      # 2. 执行旋转操作，使该子树重新恢复平衡
      return self.rotate(node)



