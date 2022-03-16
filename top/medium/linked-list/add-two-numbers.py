from typing import Optional
from ListNode import ListNode, ll_from_array


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        rest = 0

        while l1 and l2:
            res = l1.val + l2.val + rest
            if res > 9:
                rest = 1
                res = res % 10
            else:
                rest = 0
            current.next = ListNode(res)
            current = current.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            res = l1.val + rest
            if res > 9:
                rest = 1
                res = res % 10
            else:
                rest = 0
            current.next = ListNode(res)
            current = current.next
            l1 = l1.next

        while l2:
            res = l2.val + rest
            if res > 9:
                rest = 1
                res = res % 10
            else:
                rest = 0
            current.next = ListNode(res)
            current = current.next
            l2 = l2.next

        if rest:
            current.next = ListNode(rest)

        return dummy.next


solution = Solution()
assert solution.addTwoNumbers(ll_from_array([2, 4, 3]), ll_from_array([5, 6, 4])).to_arr() == [7, 0, 8]
assert solution.addTwoNumbers(ll_from_array([0]), ll_from_array([0])).to_arr() == [0]
assert solution.addTwoNumbers(ll_from_array([9, 9, 9, 9, 9, 9, 9]), ll_from_array([9, 9, 9, 9])).to_arr() == [8, 9, 9, 9, 0, 0, 0, 1]
