'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        c1, c2 = list1, list2

        while c1 and c2:
            if c1.val <= c2.val:
                current.next = c1
                c1 = c1.next
            else:
                current.next = c2
                c2 = c2.next
            current = current.next

        if c1:
            current.next = c1
        else:
            current.next = c2

        return dummy.next


solution = Solution()

list1 = ll_from_array([1, 2, 4])
list2 = ll_from_array([1, 3, 4])
result = solution.mergeTwoLists(list1, list2)
assert array_from_ll(result) == [1, 1, 2, 3, 4, 4]

list1 = ll_from_array([])
list2 = ll_from_array([])
result = solution.mergeTwoLists(list1, list2)
assert array_from_ll(result) == []

list1 = ll_from_array([])
list2 = ll_from_array([0])
result = solution.mergeTwoLists(list1, list2)
assert array_from_ll(result) == [0]
