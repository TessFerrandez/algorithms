from typing import List


class Solution:
    def kWeakestRows1(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [(sum(mat[i]), i) for i in range(len(mat))]
        soldiers.sort()
        return [soldiers[i][1] for i in range(k)]

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = sorted(range(len(mat)), key=lambda i: (mat[i], i))
        return soldiers[:k]


solution = Solution()
assert solution.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3) == [2, 0, 3]
assert solution.kWeakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], 2) == [0, 2]
