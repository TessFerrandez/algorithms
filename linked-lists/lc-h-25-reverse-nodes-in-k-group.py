from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_list(first, n) -> Optional[ListNode]:
            current = first
            previous = None
            for _ in range(n):
                next = current.next
                current.next = previous
                previous = current
                current = next
            return previous

        dummy = ListNode(0, head)
        prev = dummy

        while True:
            start = prev.next

            next = start
            for _ in range(k):
                if not next:
                    return dummy.next
                next = next.next

            first = reverse_list(start, k)
            prev.next = first
            start.next = next
            prev = start


solution = Solution()
ll = ll_from_array([1, 2, 3, 4, 5])
print(array_from_ll(solution.reverseKGroup(ll, 3)))
ll = ll_from_array([1, 2, 3, 4, 5])
print(array_from_ll(solution.reverseKGroup(ll, 2)))
