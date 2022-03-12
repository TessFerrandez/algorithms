from typing import Optional
from ListNode import ListNode, ll_from_array


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


solution = Solution()
assert solution.removeNthFromEnd(ll_from_array([1, 2, 3, 4, 5]), 2).to_arr() == [1, 2, 3, 5]
assert solution.removeNthFromEnd(ll_from_array([1]), 1) is None
assert solution.removeNthFromEnd(ll_from_array([1, 2]), 1).to_arr() == [1]
