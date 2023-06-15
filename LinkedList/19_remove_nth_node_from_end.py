class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy

        # method 1
        for _ in range(n):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        # method 2
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next
        # time complexity: O(n)
        # space complexity: O(1)

# method 3
# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        if not head:
            return None
        dummy = ListNode(val=0, next=head)
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        n = length - n
        cur = dummy
        while n:
            cur = cur.next
            n -= 1
        cur.next = cur.next.next
        return dummy.next
