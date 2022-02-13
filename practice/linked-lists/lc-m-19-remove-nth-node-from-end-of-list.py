'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0

        current = head
        while current:
            current = current.next
            count += 1

        if count == n:
            return head.next

        current = head
        for _ in range(count - n - 1):
            current = current.next
        current.next = current.next.next

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        # move the fast pointer n steps ahead
        for i in range(n):
            if not fast.next:
                # if n was the number of nodes
                # just return head.next
                if i == n - 1:
                    return head.next
            fast = fast.next

        # loop until fast reaches the end (slow will be at len - n)
        while fast.next:
            slow = slow.next
            fast = fast.next

        # remove the -nth node
        if slow.next:
            slow.next = slow.next.next

        return head


solution = Solution()
assert array_from_ll(solution.removeNthFromEnd(ll_from_array([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
assert array_from_ll(solution.removeNthFromEnd(ll_from_array([1]), 1)) == []
assert array_from_ll(solution.removeNthFromEnd(ll_from_array([1, 2]), 1)) == [1]
