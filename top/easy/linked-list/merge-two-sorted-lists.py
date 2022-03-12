from typing import Optional
from ListNode import ListNode, ll_from_array


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
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
assert solution.mergeTwoLists(None, ll_from_array([0])).to_arr() == [0]
assert solution.mergeTwoLists(ll_from_array([1, 2, 4]), ll_from_array([1, 3, 4])).to_arr() == [1, 1, 2, 3, 4, 4]
assert solution.mergeTwoLists(None, None) is None
