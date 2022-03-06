'''
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node.

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
'''
from collections import defaultdict
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        from_nodes = defaultdict(set)

        supplies = []
        for i in range(n):
            if len(graph[i]) == 0:
                supplies.append(i)
            for j in graph[i]:
                from_nodes[j].add(i)

        safe = []
        while supplies:
            node = supplies.pop()
            safe.append(node)
            for i in from_nodes[node]:
                graph[i].remove(node)
                if len(graph[i]) == 0:
                    supplies.append(i)

        return sorted(safe)


solution = Solution()
assert solution.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) == [2, 4, 5, 6]
assert solution.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]) == [4]
