'''
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.
'''
from collections import defaultdict
from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        graph = defaultdict(set)
        for i, j in connections:
            graph[i].add(j)
            graph[j].add(i)

        visited = set()

        def dfs(i):
            if i in visited:
                return 0
            visited.add(i)
            for j in graph[i]:
                dfs(j)
            return 1

        num_separate_networks = sum(dfs(i) for i in range(n))
        return num_separate_networks - 1


solution = Solution()
assert solution.makeConnected(4, [[0,1],[0,2],[1,2]]) == 1
assert solution.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]) == 2
assert solution.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]) == -1
