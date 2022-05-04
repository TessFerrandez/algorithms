from typing import List


class Solution:
    # O(n log n) - due to sort [TEMPLATE 1]
    def maxFrequency1(self, nums: List[int], k: int) -> int:
        '''
        Ex [1, 4, 8, 13] k = 5
        left    right   subsum  num     Calculation
        0       0       1       1       1 * 1 - 1 = 0
        0       1       5       4       2 * 4 - 5 = 3
        0       2       13      8       3 * 8 - 13 = 11 > 5 (bad)
        1       2       12      8       2 * 8 - 12 = 4
        1       3       25      13      3 * 13 - 25 = 11 > 5 (bad)
        2       3       21      13      2 * 13 - 21 = 5

        The longest streak of equal numbers would be 2
        - any 3 streaks require too many incs
        '''
        nums.sort()
        sub_sum, left, result = 0, 0, 0

        for right, num in enumerate(nums):
            sub_sum += num
            while (right - left + 1) * num - sub_sum > k:
                sub_sum -= nums[left]
                left += 1
            result = max(result, right - left + 1)
        return result


solution = Solution()
assert solution.maxFrequency([1, 2, 4], 5) == 3
assert solution.maxFrequency([1, 4, 8, 13], 5) == 2
assert solution.maxFrequency([3, 9, 6], 2) == 1
