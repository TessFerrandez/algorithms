'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''
from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_list(node: Optional[ListNode]) -> Optional[ListNode]:
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

        second_head = slow.next
        slow.next = None

        # reverse second list
        second_head = reverse_list(second_head)
        current1, current2 = head, second_head

        # merge lists
        while current1 and current2:
            temp1, temp2 = current1.next, current2.next
            current1.next, current2.next = current2, temp1
            current1, current2 = temp1, temp2


solution = Solution()
ll = ll_from_array([1, 2, 3, 4])
solution.reorderList(ll)
print(array_from_ll(ll))

ll = ll_from_array([1, 2, 3, 4, 5])
solution.reorderList(ll)
print(array_from_ll(ll))
