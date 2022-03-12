from typing import List, Optional


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None

    def to_arr(self) -> List[int]:
        arr = []
        current = self
        while current:
            arr.append(current.val)
            current = current.next
        return arr


def ll_from_array(data: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy

    for val in data:
        node = ListNode(val)
        current.next = node
        current = current.next

    return dummy.next
