from ListNode import ListNode, ll_from_array, array_from_ll
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)

        dummy.next = head
        current = dummy

        # find the element before the nth last
        slow = fast = current
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # remove the nth last element
        slow.next = slow.next.next
        return dummy.next


solution = Solution()
ll = ll_from_array([1, 2, 3, 4, 5])
assert array_from_ll(solution.removeNthFromEnd(ll, 2)) == [1, 2, 3, 5]

ll = ll_from_array([1])
assert array_from_ll(solution.removeNthFromEnd(ll, 1)) == []

ll = ll_from_array([1, 2])
assert array_from_ll(solution.removeNthFromEnd(ll, 1)) == [1]
