from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        new_arr = []
        for i in range(n // 2):
            if i % 2 == 0:
                new_arr.append(min(nums[2 * i: 2 * i + 2]))
            else:
                new_arr.append(max(nums[2 * i: 2 * i + 2]))

        return self.minMaxGame(new_arr)


solution = Solution()
assert solution.minMaxGame([1, 3, 5, 2, 4, 8, 2, 2]) == 1
assert solution.minMaxGame([3]) == 3
