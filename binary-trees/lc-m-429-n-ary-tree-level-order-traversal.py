from collections import deque
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        current_level, result = 0, []

        todo = deque([(1, root)])

        while todo:
            level, node = todo.popleft()
            if level > current_level:
                result.append([])
                current_level = level
            result[-1].append(node.val)
            if node.children:
                for child in node.children:
                    todo.append((level + 1, child))

        return result


solution = Solution()

tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
assert solution.levelOrder(tree) == [[1], [3, 2, 4], [5, 6]]

tree = Node(1, [Node(2), Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]), Node(4, [Node(8, [Node(12)])]), Node(5, [Node(9, [Node(13)]), Node(10)])])
assert solution.levelOrder(tree) == [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]
