from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: Optional['Node'] = None, right: Optional['Node'] = None, next: Optional['Node'] = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        prev = None
        current_level = -1
        todo = deque([(0, root)])

        while todo:
            level, node = todo.popleft()
            if level == current_level:
                prev.next = node
                prev = node
            else:
                current_level = level
                prev = node

            if node.left:
                todo.append((level + 1, node.left))
            if node.right:
                todo.append((level + 1, node.right))

        return root


solution = Solution()
root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
root = solution.connect(root)
