from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 1

        last = head
        while last.next:
            last = last.next
            n += 1

        # make list circular
        last.next = head

        # break after n - k
        current = head
        for _ in range(n - (k % n) - 1):
            current = current.next

        # break the link
        first = current.next
        current.next = None

        return first


solution = Solution()
assert array_from_ll(solution.rotateRight(ll_from_array([0, 1, 2]), 4)) == [2, 0, 1]
assert array_from_ll(solution.rotateRight(ll_from_array([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
