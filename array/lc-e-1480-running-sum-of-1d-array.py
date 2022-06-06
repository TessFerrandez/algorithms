from itertools import accumulate
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))


solution = Solution()
assert solution.runningSum([1,2,3,4]) == [1, 3, 6, 10]
assert solution.runningSum([1,1,1,1,1]) == [1, 2, 3, 4, 5]
assert solution.runningSum([3,1,2,10,1]) == [3, 4, 6, 16, 17]
