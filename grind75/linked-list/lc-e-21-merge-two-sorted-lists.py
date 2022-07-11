from typing import Optional
from ListNode import ListNode, deserialize, serialize


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2

        return dummy.next


solution = Solution()
assert serialize(solution.mergeTwoLists(deserialize([1, 2, 4]), deserialize([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
assert not solution.mergeTwoLists(None, None)
assert serialize(solution.mergeTwoLists(None, deserialize([0]))) == [0]
