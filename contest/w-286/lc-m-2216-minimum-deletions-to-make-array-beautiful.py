from typing import List


class Solution:
    def minDeletion1(self, nums: List[int]) -> int:
        nums_len, actual_idx, deletions = len(nums), 0, 0

        for i in range(len(nums) - 1):
            if actual_idx % 2 == 0 and nums[i] == nums[i + 1]:
                deletions += 1
                nums_len -= 1
                actual_idx += 1
            actual_idx += 1

        if nums_len % 2 == 1:
            deletions += 1

        return deletions

    def minDeletion(self, nums: List[int]) -> int:
        deletions = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and (i - deletions) % 2 == 0:
                deletions += 1
        return deletions + (len(nums) - deletions) % 2


solution = Solution()
assert solution.minDeletion([1, 1, 2, 2, 3, 3]) == 2
assert solution.minDeletion([1, 1, 2, 3, 5]) == 1
assert solution.minDeletion([2,6,2,5,8,9,7,2,2,5,6,2,2,0,6,8,7,3,9,2,1,1,3,2,6,2,4,6,5,8,4,8,7,0,4,8,7,8,4,1,1,4,0,1,5,7,7,5,9,7,5,5,8,6,4,3,6,5,1,6,7,6,9,9,6,8,6,0,9,5,6,7,6,9,5,5,7,3,0,0,5,5,4,8,3,9,3,4,1,7,9,3,1,8,8,9,1,6,0,0]) == 6
