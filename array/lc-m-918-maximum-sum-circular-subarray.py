from typing import List


class Solution:
    # too slow
    def maxSubarraySumCircular1(self, nums: List[int]) -> int:
        def max_sub_array(nums: List[int]) -> int:
            max_sum = - 2 ** 31
            current_sum = 0
            for num in nums:
                current_sum = max(0, current_sum + num)
                max_sum = max(max_sum, current_sum)

            return max_sum

        best = max(nums)
        if best < 0:
            return best

        best = -float('inf')

        for i in range(len(nums)):
            best = max(best, max_sub_array(nums[i:] + nums[: i]))

        return best

    # from solution
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        answer = current = -float('inf')
        for num in nums:
            current = num + max(current, 0)
            answer = max(answer, current)

        # answer is the answer for 1-interval subarrays.
        # Now, let's consider all 2-interval subarrays.
        # For each i, we want to know
        # the maximum of sum(nums[j:]) with j >= i+2

        # rightsums[i] = sum(nums[i:])
        right_sums = [-float('inf')] * n
        right_sums[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_sums[i] = right_sums[i + 1] + nums[i]

        # maxright[i] = max_{j >= i} rightsums[j]
        max_right = [-float('inf')] * n
        max_right[-1] = right_sums[-1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], right_sums[i])

        left_sum = 0
        for i in range(n - 2):
            left_sum += nums[i]
            answer = max(answer, left_sum + max_right[i + 2])

        return answer


solution = Solution()
assert solution.maxSubarraySumCircular([5, -3, 5]) == 10
assert solution.maxSubarraySumCircular([1, -2, 3, -2]) == 3
assert solution.maxSubarraySumCircular([-3, -2, -3]) == -2
