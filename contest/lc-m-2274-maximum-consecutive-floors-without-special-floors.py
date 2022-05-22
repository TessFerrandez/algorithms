from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()

        longest_streak = special[0] - bottom
        prev = special[0]

        for floor in special[1:]:
            longest_streak = max(longest_streak, floor - prev - 1)
            prev = floor

        longest_streak = max(longest_streak, top - special[-1])
        return longest_streak


solution = Solution()
assert solution.maxConsecutive(3, 15, [7, 9, 13]) == 4
assert solution.maxConsecutive(2, 9, [4, 6]) == 3
assert solution.maxConsecutive(6, 8, [7, 6, 8]) == 0
