'''
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
'''
from collections import defaultdict
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        NO_GROUP, GROUP1 = 0, 1     # GROUP2 = -1

        # dfs
        def try_assign(node_a, group):
            # assign node a to group
            group_assignment[node_a] = group

            for node_b in edges[node_a]:
                # node b is assigned to node a:s group - fail
                if group_assignment[node_b] == group:
                    return False

                # try assigning node b to the other group (-group)
                if group_assignment[node_b] == NO_GROUP and not try_assign(node_b, -group):
                    return False

            return True

        n = len(graph)
        if n == 1:
            return True

        edges = defaultdict(set)
        group_assignment = defaultdict(int)

        for node_a, neighbors in enumerate(graph):
            for node_b in neighbors:
                edges[node_a].add(node_b)

        for node in range(1, n + 1):
            if group_assignment[node] == NO_GROUP and not try_assign(node, GROUP1):
                # we can't assign node a and node b to different groups
                return False

        return True


solution = Solution()
assert not solution.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
assert solution.isBipartite([[1,3],[0,2],[1,3],[0,2]])
