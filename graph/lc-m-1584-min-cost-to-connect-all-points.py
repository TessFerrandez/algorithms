from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def union(parent, rank, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        def find(parent, node):
            if parent[node] == node:
                return node
            return find(parent, parent[node])

        n = len(points)

        # build weighted edges
        graph = []
        for p1 in range(n):
            for p2 in range(p1 + 1, n):
                x1, y1 = points[p1]
                x2, y2 = points[p2]
                graph.append([p1, p2, abs(x1 - x2) + abs(y1 - y2)])

        # kruskals algorithm
        # to create a minimum spanning tree

        # 1. sort edges by weigth
        graph = sorted(graph, key=lambda edge: edge[2])

        # 2. set up parents and ranks
        parents = list(range(n))
        rank = [0] * n

        result = []
        edge_idx, edges = 0, 0

        while edges < n - 1:
            fr, to, weight = graph[edge_idx]
            edge_idx += 1

            root1 = find(parents, fr)
            root2 = find(parents, to)

            # check if from and to are in the same graph
            # if not - add the edge
            if root1 != root2:
                edges += 1
                result.append([fr, to, weight])
                union(parents, rank, root1, root2)

        # count the weights in the minimum spanning tree
        cost = sum(edge[2] for edge in result)
        return cost


solution = Solution()
solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
