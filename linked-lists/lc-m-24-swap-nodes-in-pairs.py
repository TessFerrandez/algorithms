'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
'''
from typing import Optional
from ListNode import ListNode


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        rest = head.next.next
        root = head.next
        head.next.next = head
        root.next.next = self.swapPairs(rest)
        return root
