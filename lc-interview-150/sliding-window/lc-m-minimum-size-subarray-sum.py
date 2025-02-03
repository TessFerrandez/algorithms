# array, binary search, sliding window, prefix sum
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return 0


solution = Solution()
print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  # 2
print(solution.minSubArrayLen(4, [1, 4, 4]))  # 1
print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0

2 3 1 2 4 3
2 3 1 2 (8/4)
  3 1 2 4 (10/4)
    1 2 4 (7/3)
      2 4 3 (9/3)
        4 3 (7/2)
