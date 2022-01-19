from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_btree(data: List[int], index: int=0) -> Optional[TreeNode]:
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = create_btree(data, 2 * index + 1) # [1, 3, 7, 15, ...]
        pNode.right = create_btree(data, 2 * index + 2) # [2, 5, 12, 25, ...]
    return pNode


def arr_from_btree(tree: TreeNode) -> List[int]:
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
