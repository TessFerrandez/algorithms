'''
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
'''
from typing import List


class Solution:
    # using DFS
    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
        def explore_province(graph, current, visited):
            if current in visited:
                return False

            visited.add(current)

            for neighbor in graph[current]:
                if neighbor in graph:
                    explore_province(graph, neighbor, visited)

            return True

        def parse_grid(grid):
            graph = {}

            for y, row in enumerate(grid):
                graph[y] = []
                for x, ch in enumerate(row):
                    if x != y and ch == 1:
                        graph[y].append(x)
            return graph

        graph = parse_grid(isConnected)

        count = 0
        visited = set()

        for province in graph:
            if explore_province(graph, province, visited):
                count += 1

        return count

    # using union find
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        # build graph
        root = [i for i in range(n)]
        rank = [1] * n
        count = n

        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        # union (with optimized path compression)
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1
                return -1
            return 0

        # find number of provinces
        for y in range(n):
            for x in range(y + 1, n):
                if isConnected[y][x] == 1:
                    count += union(x, y)

        return count


solution = Solution()
assert solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1
assert solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
