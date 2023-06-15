from Cython.Debugger.Tests.TestLibCython import root

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#          1                     1--> None
#         / \                  /   \
#        2   3     ----->     2---->3-->None
#       /\   /\              / \   / \
#      4  5 6  7            4-->5->6->7-->None
#    [1,2,3,4,5,6,7]  --> [1,#,2,3,#,4,5,6,7,#]


class Solution:
    def connect_queue(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        space cpmplexity o(n)
        use bfs level order traversal. In each level traversal, record the first element in queue
        let the previous node point to this node and the last node in each level don't need to change next attribute
        '''
        if not root:
            return None
        queue=[root]
        from collections import deque
        #queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size-1:
                    break
                node.next = queue[0]
        return root
    
    def connect_linkedlist(self,root):
        '''
        Use linked list and space complexity is o(1)
        two pointers first and cur. first用来确定从上到下遍历顺序，从第一层到最后一层。cur在每一层用来从左到右遍历，从最左到最右。
        '''
        if not root:
            return None
        first = root
        while first:
            cur = first
            while cur:
                # 如果左node存在
                if cur.left:
                    cur.left.next = cur.right
                # 如果右node存在，并且cur.next存在，那么右node.next指向cur.next的左node，因为cur和cur.next在同一层相邻位置
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            first = first.left
        return root