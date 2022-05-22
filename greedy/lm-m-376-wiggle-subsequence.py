from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums)) if nums[i] - nums[i - 1] != 0]
        if not diffs:
            return 1

        count = 2

        pos = diffs[0] > 0
        for diff in diffs[1:]:
            if (pos and diff < 0) or (not pos and diff > 0):
                count += 1
                pos = not pos

        return count


solution = Solution()
assert solution.wiggleMaxLength([1]) == 1
assert solution.wiggleMaxLength([1, 1]) == 1
assert solution.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
assert solution.wiggleMaxLength([1, 4, 7, 2, 5]) == 4
assert solution.wiggleMaxLength([1, 7, 4, 5, 5]) == 4
assert solution.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7
assert solution.wiggleMaxLength([1,2,3,4,5,6,7,8,9]) == 2
