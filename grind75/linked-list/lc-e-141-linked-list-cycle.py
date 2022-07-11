from typing import Optional
from ListNode import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        slow, fast = head, head
        while fast:
            slow = slow.next

            if not fast.next:
                return False

            fast = fast.next.next

            if slow == fast:
                return True

        return False


solution = Solution()
n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2
assert solution.hasCycle(n1)

n1, n2 = ListNode(1), ListNode(2)
n1.next = n2
n2.next = n1
assert solution.hasCycle(n1)

n1 = ListNode(1)
assert not solution.hasCycle(n1)
