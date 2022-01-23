'''
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
'''
from typing import Optional
from ListNode import ListNode, ll_from_array


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []

        current = head
        while current:
            values.append(current.val)
            current = current.next

        max_twin = 0
        low, high = 0, len(values) - 1
        while low < high:
            max_twin = max(max_twin, values[low] + values[high])
            low += 1
            high -= 1

        return max_twin


solution = Solution()
assert solution.pairSum(ll_from_array([5, 2, 4, 1])) == 6
assert solution.pairSum(ll_from_array([4, 2, 2, 3])) == 7
assert solution.pairSum(ll_from_array([1, 100000])) == 100001
