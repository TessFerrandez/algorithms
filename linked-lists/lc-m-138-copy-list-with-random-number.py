from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None) -> None:
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_nodes = defaultdict(lambda: Node(0, None, None))
        new_nodes[None] = None

        old_node = head
        while old_node:
            new_nodes[old_node].val = old_node.val
            new_nodes[old_node].next = new_nodes[old_node.next]
            new_nodes[old_node].random = new_nodes[old_node.random]
            old_node = old_node.next

        return new_nodes[head]


def ll_from_arr(data):
    nodes = [Node(d[0]) for d in data]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, next in enumerate(d[1] for d in data):
        if next:
            nodes[i].random = nodes[next]
    return nodes[0]


solution = Solution()
ll = solution.copyRandomList(ll_from_arr([[7,None],[13,0],[11,4],[10,2],[1,0]]))
