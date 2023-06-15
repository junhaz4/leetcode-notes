class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
定义fast和slow指针，从头结点出发，fast指针每次移动两个节点，slow指针每次移动一个节点，如果 fast 和 slow指针在途中相遇 ，说明这个链表有环
fast指针一定先进入环中，如果fast指针和slow指针相遇的话，一定是在环中相遇，如果fast指针和slow指针不相遇，说明这个链表没有环
因为fast是走两步，slow是走一步，其实相对于slow来说，fast是一个节点一个节点的靠近slow的，所以fast一定可以和slow重合

如何找到这个环的入口:
从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点， 那么当这两个指针相遇的时候就是 环形入口的节点
proof: 假设从头结点到环形入口节点 的节点数为x。 环形入口节点到 fast指针与slow指针相遇节点 节点数为y。 从相遇节点 再到环形入口节点节点数为 z
那么相遇时：slow指针走过的节点数为: x + y，fast指针走过的节点数：x + y + n (y + z)，n为fast指针在环内走了n圈才遇到slow指针,（y+z）为 一圈内节点的个数
(x + y) * 2 = x + y + n (y + z) => x = (n - 1) (y + z) + z, n>= 1
先拿n为1的情况来举例，意味着fast指针在环形里转了一圈之后，就遇到了 slow指针了, 当n为1的时候，公式就化解为 x = z

"""
class Solution:
    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        if not head:
            return None
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cur = head
                while cur != slow:
                    cur = cur.next
                    slow = slow.next
                return cur
        return None