from heapq import heappop, heappush
from typing import List, Optional
from ListNode import ListNode, deserialize, serialize


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        todo = []
        for i, node in enumerate(lists):
            if node:
                heappush(todo, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        while todo:
            _, idx, node = heappop(todo)
            current.next = node
            current = current.next
            if node.next:
                heappush(todo, (node.next.val, idx, node.next))

        return dummy.next


solution = Solution()
assert serialize(solution.mergeKLists([deserialize([1, 4, 5]), deserialize([1, 3, 4]), deserialize([2, 6])])) == [1, 1, 2, 3, 4, 4, 5, 6]
assert serialize(solution.mergeKLists([])) == []
assert serialize(solution.mergeKLists([None])) == []
