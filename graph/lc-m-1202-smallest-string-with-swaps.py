'''
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
'''
from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps1(self, s: str, pairs: List[List[int]]) -> str:
        class UnionFind:
            def __init__(self, n) -> None:
                self.root = list(range(n))

            def union(self, x, y):
                self.root[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.root[x]:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]

        uf = UnionFind(len(s))
        result = []
        graph = defaultdict(list)

        for x, y in pairs:
            uf.union(x, y)

        for i in range(len(s)):
            graph[uf.find(i)].append(s[i])

        for comp_id in graph.keys():
            graph[comp_id].sort(reverse=True)

        for i in range(len(s)):
            result.append(graph[uf.find(i)].pop())

        return ''.join(result)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        roots = list(range(n))

        def union(node1, node2):
            roots[find(node1)] = find(node2)

        def find(node):
            if node != roots[node]:
                roots[node] = find(roots[node])
            return roots[node]

        result = []
        graph = defaultdict(list)

        for node1, node2 in pairs:
            union(node1, node2)

        for i in range(n):
            graph[find(i)].append(s[i])

        for group in graph.keys():
            graph[group].sort(reverse=True)

        for i in range(n):
            result.append(graph[find(i)].pop())

        return ''.join(result)


solution = Solution()
assert solution.smallestStringWithSwaps('dcab', [[0, 3], [1, 2]]) == 'bacd'
assert solution.smallestStringWithSwaps('dcab', [[0, 3], [1, 2], [0, 2]]) == 'abcd'
assert solution.smallestStringWithSwaps('cba', [[0, 1], [1, 2]]) == 'abc'
