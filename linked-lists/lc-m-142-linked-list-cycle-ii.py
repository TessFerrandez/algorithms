'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
'''
from typing import Optional
from ListNode import ListNode, ll_from_array_with_cycle, ll_from_array


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        seen = set()

        while current:
            if current in seen:
                return current
            seen.add(current)
            current = current.next

        return None


solution = Solution()
ll = ll_from_array_with_cycle([3, 2, 0, 4], 1)
assert solution.detectCycle(ll).val == 2

ll = ll_from_array_with_cycle([1, 2], 0)
assert solution.detectCycle(ll).val == 1

ll = ll_from_array([1])
assert solution.detectCycle(ll) is None
