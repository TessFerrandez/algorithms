from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) - k
        lowest = w_sum = sum(cardPoints[:n])
        for i in range(1, len(cardPoints) - n + 1):
            w_sum -= cardPoints[i - 1]
            w_sum += cardPoints[i + n - 1]
            lowest = min(w_sum, lowest)
        return sum(cardPoints) - lowest


solution = Solution()
assert solution.maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12
assert solution.maxScore([2, 2, 2], 2) == 4
assert solution.maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55
