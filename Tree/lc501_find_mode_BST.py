# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findMode(self, root) ->list:
        # Method 1 Recursion to find mode
        '''
        The idea is to traversal the tree only once and find the mode. Initialize count and maxcount
        if count==maxcount, put the current node into the result list. If the count>maxcount, update maxcount
        and clear the current result list because all element in result are not working.
        use pointer to indicate the previous node and the current node 
        '''
        self.count = 0
        self.max = 0
        self.result = []
        self.prev = None
        def searchBST(cur):
            if not cur:
                return 
            searchBST(cur.left)
            # the first node 
            if self.prev == None:
                self.count = 1
            # same val as the previous node
            elif self.pre.val == cur.val:
                self.count += 1
            # different val to the previous node
            else:
                self.count =1
            if self.count == self.max:
                self.result.append(cur.val)
            if self.count > self.max:
                self.max = self.count
                self.result =[cur.val]
            searchBST(cur.right)
            return 
        searchBST(root)
        return self.result 
    
        # Method 2 Iteration with stack
        count = 0
        maxcount = 0
        result = []
        stack = []
        prev = None
        cur = root
        while cur or stack:
            # first pointer to the bottom left node
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                # deal with each node
                cur = stack.pop()
                # first node
                if prev==None:
                    count =1
                elif prev.val == cur.val:
                    count += 1
                else:
                    count = 1
                if count == maxcount:
                    result.append(cur.val)
                if count > maxcount:
                    maxcount = count
                    result = [cur.val]
                pre = cur
                cur = cur.right
        return result