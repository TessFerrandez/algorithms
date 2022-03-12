from typing import Optional
from ListNode import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while slow and fast:
            slow = slow.next

            if not fast.next:
                return False

            fast = fast.next.next

            if slow == fast:
                return True

        return False


solution = Solution()

one, two, three, four = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
one.next = two
two.next = three
three.next = four
four.next = two
assert solution.hasCycle(one)

one, two = ListNode(1), ListNode(2)
one.next = two
two.next = one
assert solution.hasCycle(one)

assert not solution.hasCycle(ListNode(1))
