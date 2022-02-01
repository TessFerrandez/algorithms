'''
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''
from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = head

        while node and node.val == val:
            node = node.next

        head = node

        while node:
            while node.next and node.next.val == val:
                node.next = node.next.next
            node = node.next

        return head


solution = Solution()
assert array_from_ll(solution.removeElements(ll_from_array([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
assert array_from_ll(solution.removeElements(ll_from_array([]), 1)) == []
assert array_from_ll(solution.removeElements(ll_from_array([7, 7, 7, 7]), 7)) == []
