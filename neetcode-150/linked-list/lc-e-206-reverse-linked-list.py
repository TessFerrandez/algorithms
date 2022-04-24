from typing import Optional
from ListNode import ListNode, array_from_ll, ll_from_array


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            current = head
            head = head.next
            current.next = prev
            prev = current

        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node, prev=None):
            if not node:
                return prev
            next = node.next
            node.next = prev
            return reverse(next, node)

        return reverse(head)


solution = Solution()
assert array_from_ll(solution.reverseList(ll_from_array([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
assert array_from_ll(solution.reverseList(ll_from_array([1, 2]))) == [2, 1]
assert array_from_ll(solution.reverseList(ll_from_array([]))) == []
