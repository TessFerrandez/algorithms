from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head

        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next

        return p2


solution = Solution()
assert array_from_ll(solution.middleNode(ll_from_array([1, 2, 3, 4, 5]))) == [3, 4, 5]
assert array_from_ll(solution.middleNode(ll_from_array([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
