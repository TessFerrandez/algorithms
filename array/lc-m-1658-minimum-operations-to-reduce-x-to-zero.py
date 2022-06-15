from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        current_sum, max_len = 0, 0
        start_idx = 0
        found = False

        for end_idx in range(len(nums)):
            current_sum += nums[end_idx]
            while start_idx <= end_idx and current_sum > target:
                current_sum -= nums[start_idx]
                start_idx += 1
            if current_sum == target:
                found = True
                max_len = max(max_len, end_idx - start_idx + 1)

        return len(nums) - max_len if found else -1


solution = Solution()
assert solution.minOperations([1, 1], 3) == -1
assert solution.minOperations([1, 1, 4, 2, 3], 5) == 2
assert solution.minOperations([5, 6, 7, 8, 9], 4) == -1
assert solution.minOperations([3, 2, 20, 1, 1, 3], 10) == 5
