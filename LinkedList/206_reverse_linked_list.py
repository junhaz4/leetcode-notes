class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return None
        # recursion
        def reverse(prev, cur):
            if not cur:
                return prev
            temp = cur.next
            cur.next = prev
            return reverse(cur, temp)
        return reverse(None,head)

class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return None
        # iteration
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev