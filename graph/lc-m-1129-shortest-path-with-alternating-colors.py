'''
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
'''
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for fr, to in redEdges:
            red[fr].append(to)

        for fr, to in blueEdges:
            blue[fr].append(to)

        visited = set()
        shortest_path = [-1] * n

        todo = deque([(0, 0, 0)])
        while todo:
            steps, color, node = todo.popleft()
            if (color, node) not in visited:
                visited.add((color, node))
                if shortest_path[node] == -1:
                    shortest_path[node] = steps
                if color == 0:
                    for neighbor in red[node]:
                        todo.append((steps + 1, 1, neighbor))
                    for neighbor in blue[node]:
                        todo.append((steps + 1, 2, neighbor))
                elif color == 1:
                    for neighbor in blue[node]:
                        todo.append((steps + 1, 2, neighbor))
                elif color == 2:
                    for neighbor in red[node]:
                        todo.append((steps + 1, 1, neighbor))

        return shortest_path


solution = Solution()
assert solution.shortestAlternatingPaths(3, [[0, 1], [1, 2]], []) == [0, 1, -1]
assert solution.shortestAlternatingPaths(3, [[0, 1]], [[2, 1]]) == [0, 1, -1]
