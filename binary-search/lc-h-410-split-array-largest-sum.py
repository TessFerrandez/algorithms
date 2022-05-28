from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def is_valid(target_sum):
            current_parts, current_sum = 1, 0

            for num in nums:
                current_sum += num
                if current_sum > target_sum:
                    current_sum = num
                    current_parts += 1
                    if current_parts > m:
                        return False

            return True

        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2
            if is_valid(mid):
                high = mid
            else:
                low = mid + 1

        return low


solution = Solution()
assert solution.splitArray([7, 2, 5, 10, 8], 2) == 18
assert solution.splitArray([1, 2, 3, 4, 5], 2) == 9
assert solution.splitArray([1, 4, 4], 3) == 4
