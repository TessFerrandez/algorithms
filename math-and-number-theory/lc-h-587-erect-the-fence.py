from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = sorted(map(tuple, trees), key=lambda x:(x[0], x[1]))

        def sign(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (b[0] - o[0]) * (a[1] - o[1])

        def build(points):
            hull = []
            for p in points:
                while len(hull) >= 2 and sign(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull += p,
            return hull

        return list(set(build(points) + build(points[::-1])))


solution = Solution()
assert solution.outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]) == [(2, 4), (1, 1), (2, 0), (4, 2), (3, 3)]
assert solution.outerTrees([[1,2],[2,2],[4,2]]) == [(1, 2), (4, 2), (2, 2)]
