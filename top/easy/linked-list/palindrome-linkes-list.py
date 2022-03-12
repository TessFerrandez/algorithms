from typing import Optional
from ListNode import ListNode, ll_from_array


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # odd length
        if fast:
            slow = slow.next

        slow = reverse(slow)
        fast = head

        while slow:
            if fast.val != slow.val:
                return False
            fast = fast.next
            slow = slow.next

        return True


solution = Solution()
assert solution.isPalindrome(ll_from_array([1, 2, 2, 1]))
assert not solution.isPalindrome(ll_from_array([1, 2]))
