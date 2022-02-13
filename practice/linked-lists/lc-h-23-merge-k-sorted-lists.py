'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''
from typing import Optional, List
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        lists = [node for node in lists if node is not None]

        while lists:
            min_val = 10 ** 9
            min_i = 10 ** 9
            for i, node in enumerate(lists):
                if node.val < min_val:
                    min_val = node.val
                    min_i = i
            current.next = lists[min_i]
            if lists[min_i].next is None:
                lists = lists[:min_i] + lists[min_i + 1:]
            else:
                lists[min_i] = lists[min_i].next
            current = current.next
        return dummy.next


solution = Solution()

list1 = ll_from_array([1, 4, 5])
list2 = ll_from_array([1, 3, 4])
list3 = ll_from_array([2, 6])
result = solution.mergeKLists([list1, list2, list3])
assert array_from_ll(result) == [1, 1, 2, 3, 4, 4, 5, 6]

result = solution.mergeKLists([])
assert array_from_ll(result) == []

list1 = ll_from_array([])
result = solution.mergeKLists([list1])
assert array_from_ll(result) == []
