'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
'''
from ListNode import ListNode, ll_from_array


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        num = ''
        current = head
        while current:
            num += str(current.val)
            current = current.next
        return int(num, 2)


solution = Solution()
assert solution.getDecimalValue(ll_from_array([1, 0, 1])) == 5
assert solution.getDecimalValue(ll_from_array([0])) == 0
