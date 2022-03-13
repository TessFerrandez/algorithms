'''
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.
'''
from collections import defaultdict
from typing import List
from heapq import heappush, heappop


class Solution:
    # my solution -- misses common paths
    def minimumWeight2(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def find_all_paths(graph, start, end, path=None, pathlen=0):
            if path is None:
                path = []
            path = path + [start]
            if start == end:
                yield pathlen, path
            if start not in graph:
                yield 0, []
                return

            for node, val in graph[start].items():
                if node not in path:
                    yield from find_all_paths(graph, node, end, path, pathlen + val)

        graph = defaultdict(dict)
        for f, t, w in edges:
            if t not in graph[f]:
                graph[f][t] = w
            if t in graph[f] and graph[f][t] > w:
                graph[f][t] = w

        best_both = 10 ** 32
        best_one = 10 ** 32
        for pathlen, path in sorted(find_all_paths(graph, src1, dest)):
            if pathlen != 0:
                if src2 in path:
                    best_both = min(best_both, pathlen)
                best_one = min(best_one, pathlen)

        best_two = 10 ** 32
        for pathlen, path in sorted(find_all_paths(graph, src2, dest)):
            if pathlen != 0:
                if src1 in path:
                    best_both = min(best_both, pathlen)
                best_two = min(best_two, pathlen)

        best = min(best_both, best_one + best_two)
        if best >= 10 ** 32:
            return -1
        return best

    # solution based on others
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def dijkstra(graph, src):
            dist = [float('inf')] * n
            todo = [(0, src)]
            dist[src] = 0

            while todo:
                cost, node = heappop(todo)

                if cost > dist[node]:
                    continue

                for neighbor, weight in graph[node]:
                    cost_neighbor = cost + weight
                    if cost_neighbor < dist[neighbor]:
                        heappush(todo, (cost_neighbor, neighbor))
                        dist[neighbor] = cost_neighbor

            return dist

        graph = [[] for _ in range(n)]
        rev_graph = [[] for _ in range(n)]

        for fr, to, weight in edges:
            graph[fr].append((to, weight))
            rev_graph[to].append((fr, weight))

        dist_from_src1 = dijkstra(graph, src1)
        dist_from_src2 = dijkstra(graph, src2)
        dist_from_dest = dijkstra(rev_graph, dest)

        min_weight = min(dist_from_src1[node] + dist_from_src2[node] + dist_from_dest[node] for node in range(n))

        return min_weight if min_weight < float('inf') else -1


solution = Solution()
assert solution.minimumWeight(5, [[4,2,20],[4,3,46],[0,1,15],[0,1,43],[0,1,32],[3,1,13]], 0, 4, 1) == 74
assert solution.minimumWeight(8, [[4,7,24],[1,3,30],[4,0,31],[1,2,31],[1,5,18],[1,6,19],[4,6,25],[5,6,32],[0,6,50]], 4, 1, 6) == 44
assert solution.minimumWeight(6, [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], 0, 1, 5) == 9
assert solution.minimumWeight(3, [[0,1,1],[2,1,1]], 0, 1, 2) == -1
assert solution.minimumWeight(5, [[0,2,1],[0,3,1],[2,4,1],[3,4,1],[1,2,1],[1,3,10]], 0, 1, 4) == 3
