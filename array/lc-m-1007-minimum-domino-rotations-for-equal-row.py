from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        top, bottom = tops[0], bottoms[0]
        top1, top2, bottom1, bottom2 = 0, 0, 0, 0

        for i in range(len(tops)):
            if top != tops[i] and top != bottoms[i]:
                top = -1
            else:
                top1 += 1 if top == tops[i] else 0
                top2 += 1 if top == bottoms[i] else 0

            if bottom != tops[i] and bottom != bottoms[i]:
                bottom = -1
            else:
                bottom1 += 1 if bottom == tops[i] else 0
                bottom2 += 1 if bottom == bottoms[i] else 0

            if top == -1 and bottom == -1:
                return -1

        best = 10 ** 9
        if top != -1:
            best = min(best, n - max(top1, top2))
        if bottom != -1:
            best = min(best, n - max(bottom1, bottom2))
        return best


solution = Solution()
assert solution.minDominoRotations([1, 2, 3, 4, 6], [6, 6, 6, 6, 5]) == 1
assert solution.minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]) == 2
assert solution.minDominoRotations([3, 5, 1, 2, 3], [3, 6, 3, 3, 4]) == -1
