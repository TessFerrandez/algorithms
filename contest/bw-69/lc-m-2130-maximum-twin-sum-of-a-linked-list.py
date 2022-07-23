from typing import Optional
from ListNode import ListNode, deserialize


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        before = []

        while fast and fast.next:
            before.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        max_twin_sum = 0

        while before:
            a = before.pop()
            b = slow.val
            max_twin_sum = max(max_twin_sum, a + b)
            slow = slow.next

        return max_twin_sum


solution = Solution()
assert solution.pairSum(deserialize([5, 4, 2, 1])) == 6
assert solution.pairSum(deserialize([4, 2, 2, 3])) == 7
assert solution.pairSum(deserialize([1, 100000])) == 100001
