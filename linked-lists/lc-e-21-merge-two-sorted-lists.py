from typing import Optional
from ListNode import ListNode, array_from_ll, ll_from_array


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next

        while l1:
            current.next = ListNode(l1.val)
            l1 = l1.next
            current = current.next

        while l2:
            current.next = ListNode(l2.val)
            l2 = l2.next
            current = current.next

        return dummy.next


solution = Solution()
print(array_from_ll(solution.mergeTwoLists(ll_from_array([1, 2, 4]), ll_from_array([1, 3, 4]))))
print(array_from_ll(solution.mergeTwoLists(ll_from_array([]), ll_from_array([]))))
print(array_from_ll(solution.mergeTwoLists(ll_from_array([]), ll_from_array([0]))))
