from typing import Optional
from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        arr.sort()
        head = ListNode(arr[0])
        current = head
        for num in arr[1:]:
            current.next = ListNode(num)
            current = current.next

        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1, list2):
            dummy = ListNode(0)
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

        def get_mid(head):
            mid_prev = None
            while head and head.next:
                mid_prev = head if mid_prev is None else mid_prev.next
                head = head.next.next
            mid = mid_prev.next
            mid_prev.next = None
            return mid

        if head is None or head.next is None:
            return head

        mid = get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)


solution = Solution()
assert array_from_ll(solution.sortList(ll_from_array([4, 2, 1, 3]))) == [1, 2, 3, 4]
assert array_from_ll(solution.sortList(ll_from_array([-1, 5, 3, 4, 0]))) == [-1, 0, 3, 4, 5]
assert array_from_ll(solution.sortList(ll_from_array([]))) == []
