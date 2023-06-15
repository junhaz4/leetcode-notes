# 105 is a similar problem, construct tree from preorder and inorder 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder:list, postorder:list) -> TreeNode:
        '''
        use recursion to contruct tree, input is the inorder and postorder list and return value is treenode
        since the return value of original function is treenode, can just use it no need for helper function
        1. if any node is empty, return none
        2. take the last element from postorder as the seperator
        3. find the index of seperator and seperate the inorder list into left and right sublist
        4. seperate the postorder list into left and right sublist 
        5. recursively contruct left subtree and right subtree
        
        ex: inorder = [9,3,15,20,7]  postorder = [9,15,7,20,3]
        find pick 3 as the seperator and then seperate two lists into
                             [9  3  15 20 7]
                             [9 15 7 20  3]   3 is seperator (root)
                             /            \
                           [9]           [15  20  7]
                           [9]           [15 7 20]   20 is seperator (root) 
                                         /       \
                                        [15]     [7]
                                        [15]     [7]
        '''
        if not inorder or not postorder:
            return None
        # find seperator and its index in inorder list 
        val = postorder[-1]
        root = TreeNode(val)
        index = inorder.index(val)
        # seperate inorder list 
        left_in =inorder[:index]
        right_in = inorder[index+1:]
        # seperate postorder list 
        # left post sublist should have the same length as left in sublist 
        left_post = postorder[:len(left_in)]
        right_post = postorder[len(left_in):len(postorder)-1]
        # recursive call to construct left and right subtree
        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)
        return root