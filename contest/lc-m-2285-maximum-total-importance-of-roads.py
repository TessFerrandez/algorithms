from collections import defaultdict
from typing import List


class Solution:
    # my solution during contest
    def maximumImportance1(self, n: int, roads: List[List[int]]) -> int:
        road_counts = defaultdict(int)

        for x, y in roads:
            road_counts[x] += 1
            road_counts[y] += 1

        nodes = [(road_counts[i], i) for i in range(n)]
        nodes.sort()

        new_index = {}
        for j, (_, i) in enumerate(nodes):
            new_index[i] = j + 1

        total = 0
        for x, y in roads:
            total += new_index[x] + new_index[y]

        return total

    # simplified
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        road_counts = defaultdict(int)
        for n1, n2 in roads:
            road_counts[n1] += 1
            road_counts[n2] += 1

        nodes = sorted([(roads, node) for node, roads in road_counts.items()])
        return sum(count * (i + 1) for i, (count, _) in enumerate(nodes))


solution = Solution()
assert solution.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]) == 43
assert solution.maximumImportance(5, [[0,3],[2,4],[1,3]]) == 20
