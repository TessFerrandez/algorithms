from typing import List, Optional
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def create_btree(data: List[int], index: int) -> Optional[Node]:
    pNode = None
    if index < len(data):
        if data[index] is None:
            return
        pNode = Node(data[index])
        pNode.left = create_btree(data, 2 * index + 1)      # [1, 3, 7, 15, ...]
        pNode.right = create_btree(data, 2 * index + 2)     # [2, 5, 12, 25, ...]
    return pNode


def serialize(tree: Node) -> List:
    arr = []
    todo = deque([tree])

    while todo:
        current = todo.popleft()
        if current:
            arr.append(current.val)
            if not current.next:
                arr.append('#')
            todo.append(current.left)
            todo.append(current.right)
        else:
            arr.append(None)

    while arr[-1] is None:
        arr = arr[:-1]
    return arr


# tree = create_btree([1, 2, 3, 4, 5, 6, 7], 0)
# print(serialize(tree))
