from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = [""] * n

        scores = sorted([(num, i) for i, num in enumerate(score)])[::-1]
        result[scores[0][1]] = 'Gold Medal'
        if n > 1:
            result[scores[1][1]] = 'Silver Medal'
        if n > 2:
            result[scores[2][1]] = 'Bronze Medal'
        for i in range(3, n):
            result[scores[i][1]] = str(i + 1)

        return result


solution = Solution()
assert solution.findRelativeRanks([5,4,3,2,1]) == ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
assert solution.findRelativeRanks([10,3,8,9,4]) == ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
