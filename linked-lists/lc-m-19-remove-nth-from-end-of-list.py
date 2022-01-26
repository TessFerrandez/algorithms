from typing import Optional
from ListNode import ListNode, array_from_ll, ll_from_array


class Solution:
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head

        nodes = []
        while current:
            nodes.append(current)
            current = current.next

        node_len = len(nodes)
        if n == node_len:
            if head and head.next:
                head = head.next
            else:
                head = None
        elif node_len - n - 1 >= 0:
            current = nodes[node_len - n - 1]
            current.next = current.next.next

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head

        # count nodes
        count = 0
        while current:
            count += 1
            current = current.next

        # from front = count - n
        pos = count - n

        if pos == 0:
            if head:
                return head.next
            else:
                return None
        else:
            current = head
            for _ in range(pos - 1):
                current = current.next
            current.next = current.next.next

        return head


solution = Solution()
assert array_from_ll(solution.removeNthFromEnd(ll_from_array([1, 2]), 2)) == [2]
assert array_from_ll(solution.removeNthFromEnd(ll_from_array([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
assert array_from_ll(solution.removeNthFromEnd(ll_from_array([1]), 1)) == []
assert array_from_ll(solution.removeNthFromEnd(ll_from_array([1, 2]), 1)) == [1]
