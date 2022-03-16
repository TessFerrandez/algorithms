from typing import Optional
from ListNode import ListNode, ll_from_array


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        jump = 1

        while current:
            prev = current
            for _ in range(jump):
                prev = prev.next
                if prev is None or prev.next is None:
                    return head
            nn = prev.next
            even = current.next
            prev.next = nn.next
            nn.next = even
            current.next = nn
            current = current.next
            jump += 1

        return head


solution = Solution()
print(solution.oddEvenList(ll_from_array([1,2,3,4,5,6,7,8])).to_arr())
assert solution.oddEvenList(ll_from_array([1, 2, 3, 4, 5])).to_arr() == [1, 3, 5, 2, 4]
assert solution.oddEvenList(ll_from_array([2, 1, 3, 5, 6, 4, 7])).to_arr() == [2, 3, 6, 7, 1, 5, 4]
