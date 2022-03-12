from typing import Optional
from ListNode import ListNode, ll_from_array


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head
        prev = None

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev


solution = Solution()
assert solution.reverseList(ll_from_array([1, 2, 3, 4, 5])).to_arr() == [5, 4, 3, 2, 1]
assert solution.reverseList(ll_from_array([1, 2])).to_arr() == [2, 1]
assert solution.reverseList(ll_from_array([])) is None
