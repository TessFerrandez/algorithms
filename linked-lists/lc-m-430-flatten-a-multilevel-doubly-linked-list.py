from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        while current:
            if current.child:
                tail = current.next
                current.next = self.flatten(current.child)
                current.next.prev = current
                current.child = None

                while current.next:
                    current = current.next

                current.next = tail
                if tail:
                    tail.prev = current

            current = current.next

        return head


def build_first_list():
    nodes = [None] * 13
    for i in range(1, 13):
        nodes[i] = Node(i, nodes[i - 1], None, None)

    for i in range(1, 12):
        nodes[i].next = nodes[i + 1]

    nodes[6].next = None
    nodes[7].prev = None
    nodes[10].next = None
    nodes[11].prev = None
    nodes[12].next = None
    nodes[3].child = nodes[7]
    nodes[8].child = nodes[11]
    return nodes[1]

solution = Solution()
first = build_first_list()
after = solution.flatten(first)
print("hello")
