from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def find(self, val):
        if self.val == val:
            return self
        if self.left:
            node = self.left.find(val)
            if node:
                return node
        if self.right:
            node = self.right.find(val)
            if node:
                return node
        return None


def deserialize(data: List[Optional[int]]) -> Optional[TreeNode]:
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


def create_btree(data: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    pNode = None
    if index < len(data):
        if data[index] is None:
            return
        pNode = TreeNode(data[index])
        pNode.left = create_btree(data, 2 * index + 1)      # [1, 3, 7, 15, ...]
        pNode.right = create_btree(data, 2 * index + 2)     # [2, 5, 12, 25, ...]
    return pNode


def serialize(tree: TreeNode) -> List[int]:
    if not tree:
        return []
    arr = []
    todo = deque([tree])

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
