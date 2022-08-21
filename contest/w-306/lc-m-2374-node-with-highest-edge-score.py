from collections import defaultdict
from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        if not edges:
            return 0

        nodes = defaultdict(int)

        for i, to in enumerate(edges):
            nodes[to] += i
        nodes = sorted([(nodes[node], node) for node in range(len(edges))], key=lambda x: (-x[0], x[1]))
        return nodes[0][1]


solution = Solution()
assert solution.edgeScore([1,0,0,0,0,7,7,5]) == 7
assert solution.edgeScore([2,0,0,2]) == 0
