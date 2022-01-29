'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
'''
from typing import List


class Solution:
    def allPathsSourceTarget(self, nodes: List[List[int]]) -> List[List[int]]:
        def parse_graph(nodes):
            graph = {}

            for i, targets in enumerate(nodes):
                graph[i] = targets

            return graph

        def find_all_paths(graph, start, target):
            if start == target:
                return [[target]]

            paths = []
            for next_node in graph[start]:
                for p in find_all_paths(graph, next_node, target):
                    paths.append([start] + p)

            return paths

        max_node = len(nodes) - 1
        graph = parse_graph(nodes)

        return find_all_paths(graph, 0, max_node)


solution = Solution()
assert solution.allPathsSourceTarget([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
assert solution.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
