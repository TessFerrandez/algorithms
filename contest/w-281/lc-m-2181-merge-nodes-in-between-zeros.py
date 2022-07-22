from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head
        current = head

        while current:
            c2 = current.next
            while c2.val != 0:
                current.val += c2.val
                c2 = c2.next
            if c2.next:
                current.next = c2
            else:
                current.next = None
                c2 = None
            current = c2
        return head


solution = Solution()
ll = ll_from_array([0, 3, 1, 0, 4, 5, 2, 0])
print(array_from_ll(solution.mergeNodes(ll)))

ll = ll_from_array([0,1,0,3,0,2,2,0])
print(array_from_ll(solution.mergeNodes(ll)))
