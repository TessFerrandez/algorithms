'''
Given the head of a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Return the linked list sorted as well.
'''
from typing import Optional
from ListNode import ListNode, array_from_ll, ll_from_array


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        base = ListNode(val=0, next=head)
        prev, current = base, head

        while current and current.next:
            is_duplicate = False
            while current.next and current.val == current.next.val:
                is_duplicate = True
                current.next = current.next.next
            if is_duplicate:
                prev.next = current.next
                current = prev.next
            else:
                prev, current = prev.next, current.next

        return base.next


solution = Solution()
assert array_from_ll(solution.deleteDuplicates(ll_from_array([1, 2, 3, 3, 4, 4, 5]))) == [1, 2, 5]
assert array_from_ll(solution.deleteDuplicates(ll_from_array([1, 1, 1, 2, 3]))) == [2, 3]
