from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next


solution = Solution()
l1 = ll_from_array([1, 2, 4])
l2 = ll_from_array([1, 3, 4])
assert array_from_ll(solution.mergeTwoLists(l1, l2)) == [1, 1, 2, 3, 4, 4]

l1 = ll_from_array([])
l2 = ll_from_array([])
assert array_from_ll(solution.mergeTwoLists(l1, l2)) == []

l1 = ll_from_array([])
l2 = ll_from_array([0])
assert array_from_ll(solution.mergeTwoLists(l1, l2)) == [0]
