from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(x) for x in zip(*mat[::-1])]
        return False


solution = Solution()
assert solution.findRotation([[0,1],[1,0]], [[1,0],[0,1]])
assert not solution.findRotation([[0,1],[1,1]], [[1,0],[0,1]])
