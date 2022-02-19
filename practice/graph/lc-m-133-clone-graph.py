'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
'''
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def graph_from_adj_list(adj_list):
    nodes = [Node(i + 1) for i in range(len(adj_list))]

    for i, neighbor_idxes in enumerate(adj_list):
        neighbors = [nodes[idx - 1] for idx in neighbor_idxes]
        nodes[i].neighbors = neighbors

    if nodes:
        return nodes[0]
    else:
        return None


def adj_list_from_graph(node):
    if not node:
        return []

    nodes = {}
    todo = deque([node])

    while todo:
        node = todo.popleft()
        nodes[node.val] = node

        for neighbor in node.neighbors:
            if neighbor.val not in nodes:
                todo.append(neighbor)

    adj_list = []
    for i in sorted(nodes.keys()):
        adj_list.append([neighbor.val for neighbor in nodes[i].neighbors])

    return adj_list


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        nodes = {}

        def clone(node):
            if node in nodes:
                return nodes[node]

            copy = Node(node.val)
            nodes[node] = copy
            copy.neighbors = [clone(neighbor) for neighbor in node.neighbors]
            return copy

        return clone(node)


solution = Solution()

node = graph_from_adj_list([])
copy_of_node = solution.cloneGraph(node)
assert adj_list_from_graph(copy_of_node) == []

node = graph_from_adj_list([[2, 4], [1, 3], [2, 4], [1, 3]])
copy_of_node = solution.cloneGraph(node)
assert adj_list_from_graph(copy_of_node) == [[2, 4], [1, 3], [2, 4], [1, 3]]

node = graph_from_adj_list([[]])
copy_of_node = solution.cloneGraph(node)
assert adj_list_from_graph(copy_of_node) == [[]]
