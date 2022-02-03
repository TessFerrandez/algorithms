'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
'''
from typing import Optional
from ListNode import ListNode, array_from_ll, ll_from_array


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


solution = Solution()
assert array_from_ll(solution.deleteDuplicates(ll_from_array([1, 2, 3, 3, 4, 4, 5]))) == [1, 2, 3, 4, 5]
assert array_from_ll(solution.deleteDuplicates(ll_from_array([1, 1, 1, 2, 3]))) == [1, 2, 3]
