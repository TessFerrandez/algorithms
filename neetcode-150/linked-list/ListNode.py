from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def ll_from_array(nums: List[int]) -> Optional[ListNode]:
    head = ListNode(0)
    current = head
    for num in nums:
        node = ListNode(num)
        current.next = node
        current = node

    return head.next


def ll_from_array_with_cycle(nums: List[int], pos: int) -> Optional[ListNode]:
    head = ListNode(0)

    cycle_start = None

    current = head
    for num in nums:
        node = ListNode(num)
        if pos == 0:
            cycle_start = node
        current.next = node
        current = node
        pos -= 1

    # make the cycle
    current.next = cycle_start

    return head.next


def array_from_ll(li: Optional[ListNode]) -> List:
    arr = []
    current = li

    while current:
        arr.append(current.val)
        current = current.next

    return arr
