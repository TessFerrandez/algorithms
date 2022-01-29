from Node import Node, create_btree, serialize
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        todo = deque([(root, 0)])

        while todo:
            node, level = todo.popleft()
            if todo and todo[0][1] == level:
                node.next = todo[0][0]
            if node.left:
                todo.append((node.left, level + 1))
            if node.right:
                todo.append((node.right, level + 1))

        return root


solution = Solution()
root = create_btree([1, 2, 3, 4, 5, None, 7])
root = solution.connect(root)
assert serialize(root, True) == [1, '#', 2, 3, '#', 4, 5, 7, '#']

root = create_btree([])
root = solution.connect(root)
assert serialize(root, True) == []
