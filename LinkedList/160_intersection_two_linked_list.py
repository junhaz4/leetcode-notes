class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        if not headA or not headB:
            return None
        # method 1
        """
        根据快慢法则，走的快的一定会追上走得慢的。
        在这道题里，有的链表短，他走完了就去走另一条链表，我们可以理解为走的快的指针。
        那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
        位置相遇
        """
        cur_a, cur_b = headA, headB
        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB
            cur_b = cur_b.next if cur_b else headA
        return cur_a


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        # method 2
        if not headA or not headB:
            return None
        cur_a, cur_b = headA, headB
        len_a, len_b = 0, 0
        while cur_a: # find length of A
            len_a += 1
            cur_a = cur_a.next
        while cur_b: # find length of B
            len_b += 1
            cur_b = cur_b.next

        cur_a, cur_b = headA, headB
        if len_b > len_a:  # 让curA为最长链表的头，lenA为其长度
            len_a, len_b = len_b, len_a
            cur_a, cur_b = cur_b, cur_a
        diff = len_a - len_b
        while diff: # 让curA和curB在同一起点上（末尾位置对齐）
            cur_a = cur_a.next
            diff -= 1
        while cur_a: # 遍历curA 和 curB，遇到相同则直接返回
            if cur_a == cur_b:
                return cur_a
            cur_a = cur_a.next
            cur_b = cur_b.next
        return None
