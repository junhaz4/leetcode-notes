class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: [ListNode]) -> [ListNode]:
        # tine: O(n)
        # space: O(1)
        if not head:
            return None
        dummy = cur = ListNode(val=0,next=head)
        while cur.next and cur.next.next:
            temp1 = cur.next
            temp2 = cur.next.next

            temp1.next = temp2.next
            temp2.next = temp1
            cur.next = temp2
            cur = cur.next.next
        return dummy.next