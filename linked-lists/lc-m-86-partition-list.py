from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_head = smaller = ListNode()
        bigger_head = bigger = ListNode()
        current = head

        while current:
            if current.val >= x:
                bigger.next = current
                bigger = bigger.next
            else:
                smaller.next = current
                smaller = smaller.next
            current = current.next

        bigger.next = None
        smaller.next = bigger_head.next
        return smaller_head.next


solution = Solution()
assert array_from_ll(solution.partition(ll_from_array([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]
assert array_from_ll(solution.partition(ll_from_array([2, 1]), 2)) == [1, 2]
