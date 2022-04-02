from typing import List


class Solution:
    def triangularSum1(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums

        return nums[0]

    # Space O(1)
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        while n > 1:
            for i in range(n - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            n -= 1

        return nums[0]


solution = Solution()
assert solution.triangularSum([5 for _ in range(1000)]) == 0
assert solution.triangularSum([1, 2, 3, 4, 5]) == 8
assert solution.triangularSum([5]) == 5
