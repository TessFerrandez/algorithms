from typing import Counter, List


class UnionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        counter = Counter([uf.find(i) for i in range(n)])
        group_counts = list(counter.values())

        answer = 0
        first_count = group_counts[0]
        for i in range(1, len(group_counts)):
            answer += first_count * group_counts[i]
            first_count += group_counts[i]

        return answer


solution = Solution()
assert solution.countPairs(3, [[0,1],[0,2],[1,2]]) == 0
assert solution.countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]) == 14
