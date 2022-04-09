from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow, fast = head, head

        first, second = None, None

        for _ in range(k - 1):
            fast = fast.next

        first = fast

        while fast.next:
            slow = slow.next
            fast = fast.next

        second = slow

        first.val, second.val = second.val, first.val
        return head


solution = Solution()
print(array_from_ll(solution.swapNodes(ll_from_array([1, 2, 3, 4, 5]), 2)))
