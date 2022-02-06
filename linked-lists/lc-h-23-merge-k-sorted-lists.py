'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''
from typing import List, Optional
from ListNode import ListNode, ll_from_array, array_from_ll
from heapq import heappop, heappush


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        for i, ll in enumerate(lists):
            if ll:
                # adding an extra index to compare with in case values are same in multiple lists
                # as heappush needs to know which is smaller and ll doesnt have a comparer
                heappush(heap, (ll.val, i, ll))

        dummy = ListNode()
        current = dummy

        while heap:
            _, i, node = heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next


solution = Solution()
l1 = ll_from_array([1, 4, 5])
l2 = ll_from_array([1, 3, 4])
l3 = ll_from_array([2, 6])
assert array_from_ll(solution.mergeKLists([l1, l2, l3])) == [1, 1, 2, 3, 4, 4, 5, 6]
assert array_from_ll(solution.mergeKLists([])) == []
assert array_from_ll(solution.mergeKLists([None])) == []
