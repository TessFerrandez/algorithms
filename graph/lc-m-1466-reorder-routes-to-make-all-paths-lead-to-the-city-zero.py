'''
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.
'''
from typing import List
from collections import defaultdict


def remove_reacheable(connections, reacheable):
    reacheable_edges = []
    for connection in connections:
        if connection[1] in reacheable:
            reacheable_edges.append(connection)

    for edge in reacheable_edges:
        connections.remove(edge)
        reacheable.add(edge[0])


class Solution:
    def minReorder2(self, n: int, connections: List[List[int]]) -> int:
        reacheable = set([0])

        remove_reacheable(connections, reacheable)
        num_reorders = 0

        while len(reacheable) != n:
            # find an edge that you can reverse to reach a node
            for connection in connections:
                if connection[0] in reacheable:
                    connection[0], connection[1] = connection[1], connection[0]
                    reacheable.add(connection[0])
                    num_reorders += 1
                    break
            # note which new ones are reacheable
            remove_reacheable(connections, reacheable)

        return num_reorders

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)

        for o, d in connections:
            graph[o].append(d)
            graph[d].append(o)
            roads.add((o, d))

        def dfs(node, parent):
            reorders = 0

            if (parent, node) in roads:
                reorders += 1

            for child in graph[node]:
                if child != parent:
                    reorders += dfs(child, node)

            return reorders

        return dfs(0, -1)


solution = Solution()
assert solution.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3
assert solution.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]) == 2
assert solution.minReorder(3, [[1,0],[2,0]]) == 0
