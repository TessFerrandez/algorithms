from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        todo = deque([node])
        copies = {node.val: Node(node.val, [])}

        while todo:
            current = todo.popleft()
            copy = copies[current.val]

            for neighbor in current.neighbors:
                if neighbor.val not in copies:
                    copies[neighbor.val] = Node(neighbor.val, [])
                    todo.append(neighbor)

                copy.neighbors.append(copies[neighbor.val])

        return copies[node.val]
