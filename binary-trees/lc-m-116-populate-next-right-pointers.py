from typing import Optional
from Node import Node, create_btree, serialize
from collections import deque


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root == None:
            return root

        i, n = 0, 0
        todo = deque([root])

        while todo:
            i += 1
            current = todo.popleft()

            if current:
                if i == 2 ** n:
                    n += 1
                    i = 0
                else:
                    current.next = todo[0]

                if current.left:
                    todo.append(current.left)
                if current.right:
                    todo.append(current.right)

        return root

    def connect2(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return root

        todo = deque([root])
        while todo:
            size = len(todo)

            # Iterate over all the nodes on the current level
            for i in range(size):
                node = todo.popleft()

                # connect to next on this level - for all but the last one
                if i < size - 1:
                    node.next = todo[0]

                if node.left:
                    todo.append(node.left)
                if node.right:
                    todo.append(node.right)

        return root


solution = Solution()
tree = create_btree([1, 2, 3, 4, 5, 6, 7], 0)
tree = solution.connect(tree)
print(serialize(tree))
