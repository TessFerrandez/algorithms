from collections import defaultdict
from typing import List
from UnionFind import UnionFind


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(range(n))

        for a, b in pairs:
            uf.union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            groups[uf.find(i)].append(i)

        new_s = [''] * n
        for group in groups:
            indices = sorted(groups[group])
            letters = sorted(s[i] for i in indices)
            for i, index in enumerate(indices):
                new_s[index] = letters[i]

        return ''.join(new_s)


solution = Solution()
assert solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]) == "bacd"
assert solution.smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]) == "abcd"
