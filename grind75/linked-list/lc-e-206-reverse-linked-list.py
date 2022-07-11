from typing import Optional
from ListNode import ListNode, serialize, deserialize


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next

        return previous


solution = Solution()
assert not solution.reverseList(None)
assert serialize(solution.reverseList(deserialize([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
assert serialize(solution.reverseList(deserialize([1, 2]))) == [2, 1]
