from typing import List
from UnionFind import UnionFind


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [(stone[0], stone[1]) for stone in stones]
        uf = UnionFind(stones)

        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0]:
                    uf.union(stones[i], stones[j])
                if stones[i][1] == stones[j][1]:
                    uf.union(stones[i], stones[j])

        # we can remove all stones but one in each group
        parents = set()
        for stone in stones:
            parents.add(uf.find(stone))

        return len(stones) - len(parents)


solution = Solution()
assert solution.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]) == 5
assert solution.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]) == 3
assert solution.removeStones([[0, 0]]) == 0
