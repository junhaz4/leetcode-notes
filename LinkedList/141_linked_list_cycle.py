class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # method 1: slow and fast pointers
    # time: O(n)
    # space: O(1)
    def hasCycle(self, head) -> bool:
        if not head:
            return None
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

class Solution:
    # method 2: hash table use a set to store the visited nodes
    # time: O(n)
    # space: O(n)
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False