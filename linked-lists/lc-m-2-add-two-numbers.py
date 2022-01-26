from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current = head
        rest = 0

        while l1 and l2:
            result = l1.val + l2.val + rest
            rest = 1 if result > 9 else 0
            node = ListNode(result % 10)
            current.next = node
            current = node
            l1 = l1.next
            l2 = l2.next

        while l1:
            result = l1.val + rest
            rest = 1 if result > 9 else 0
            node = ListNode(result % 10)
            current.next = node
            current = node
            l1 = l1.next

        while l2:
            result = l2.val + rest
            rest = 1 if result > 9 else 0
            node = ListNode(result % 10)
            current.next = node
            current = node
            l2 = l2.next

        if rest != 0:
            node = ListNode(rest)
            current.next = node

        return head.next


solution = Solution()

assert array_from_ll(solution.addTwoNumbers(ll_from_array([2, 4, 3]), ll_from_array([5, 6, 4]))) == [7, 0, 8]
assert array_from_ll(solution.addTwoNumbers(ll_from_array([0]), ll_from_array([0]))) == [0]
assert array_from_ll(solution.addTwoNumbers(ll_from_array([9,9,9,9,9,9,9]), ll_from_array([9,9,9,9]))) == [8,9,9,9,0,0,0,1]
