from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        if nums[0] > 0:
            pos = 1
        elif nums[0] < 0:
            neg = 1

        longest_pos = pos

        for num in nums[1:]:
            if num > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0
            elif num < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
            else:
                pos, neg = 0, 0
            longest_pos = max(longest_pos, pos)

        return longest_pos


solution = Solution()
assert solution.getMaxLen([1,-2,-3,4]) == 4
assert solution.getMaxLen([0,1,-2,-3,-4]) == 3
assert solution.getMaxLen([-1,-2,-3,0,1]) == 2
