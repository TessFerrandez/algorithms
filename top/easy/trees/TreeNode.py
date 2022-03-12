from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def to_array(self) -> List[int]:
        arr = []
        todo = deque([self])

        while todo:
            current = todo.popleft()
            if current:
                arr.append(current.val)
                todo.append(current.left)
                todo.append(current.right)
            else:
                arr.append(None)

        while arr[-1] is None:
            arr = arr[:-1]

        return arr


def from_array(data: List[Optional[int]]) -> Optional[TreeNode]:
    if data is None or data == []:
        return None

    nodes = [None if val is None else TreeNode(val) for val in data]

    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root
