'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''
from typing import Optional
from ListNode import ListNode, ll_from_array_with_cycle, ll_from_array


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while slow and fast:
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
            if slow == fast:
                return True

        return False


solution = Solution()

ll = ll_from_array_with_cycle([3, 2, 0, -4], 1)
assert solution.hasCycle(ll)

ll = ll_from_array_with_cycle([1, 2], 0)
assert solution.hasCycle(ll)

ll = ll_from_array([1, 2])
assert not solution.hasCycle(ll)

ll = ll_from_array([1])
assert not solution.hasCycle(ll)
