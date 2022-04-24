from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None
            prev, current = None, node
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        if head is None or head.next is None or head.next.next is None:
            return

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        # reverse second list
        l1, l2 = head, reverse(l2)

        # merge lists
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l1.next, l2.next = l2, temp1
            l1, l2 = temp1, temp2


solution = Solution()
ll = ll_from_array([1, 2, 3, 4])
solution.reorderList(ll)
assert array_from_ll(ll) == [1, 4, 2, 3]

ll = ll_from_array([1, 2, 3, 4, 5])
solution.reorderList(ll)
assert array_from_ll(ll) == [1, 5, 2, 4, 3]
