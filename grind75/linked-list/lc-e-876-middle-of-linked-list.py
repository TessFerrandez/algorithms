from typing import Optional
from ListNode import ListNode, serialize, deserialize


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


solution = Solution()
assert serialize(solution.middleNode(deserialize([1, 2, 3, 4, 5]))) == [3, 4, 5]
assert serialize(solution.middleNode(deserialize([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
