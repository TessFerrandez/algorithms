from functools import cache
from itertools import accumulate
from typing import List


class Solution:
    # with memoization (my solution)
    def splitArray1(self, nums: List[int], m: int) -> int:
        prefix_sum, cum_sum = 0, []
        n = len(nums)

        if m >= n:
            return max(nums)

        for num in nums:
            prefix_sum += num
            cum_sum.append(prefix_sum)

        @cache
        def split(first, m):
            prev = 0 if first == 0 else cum_sum[first - 1]

            if m == 1:
                return cum_sum[-1] - prev

            best = float('inf')
            for i in range(first, n - m + 1):
                curr_sum = cum_sum[i] - prev
                if curr_sum > best:
                    break
                rest_sum = split(i + 1, m - 1)
                best = min(best, max(curr_sum, rest_sum))

            return best

        return split(0, m)

    # bottom up dp
    def splitArray2(self, nums: List[int], m: int) -> int:
        n = len(nums)
        dp = [[0] * (m + 1) for _ in range(n)]

        cum_sum = [0] + list(accumulate(nums))

        for subarray_count in range(1, m + 1):
            for curr_i in range(n):

                if subarray_count == 1:
                    dp[curr_i][subarray_count] = cum_sum[n] - cum_sum[curr_i]
                    continue

                min_max_sum = cum_sum[n]
                for i in range(curr_i, n - subarray_count + 1):
                    first_split_sum = cum_sum[i + 1] - cum_sum[curr_i]
                    largest_split_sum = max(first_split_sum, dp[i + 1][subarray_count - 1])
                    min_max_sum = min(min_max_sum, largest_split_sum)

                    if first_split_sum >= min_max_sum:
                        break

                dp[curr_i][subarray_count] = min_max_sum

        return dp[0][m]

    # binary search
    def splitArray(self, nums: List[int], m: int) -> int:
        def min_subarrays_required(max_sum_allowed) -> int:
            current_sum = 0
            splits_required = 0

            for num in nums:
                if current_sum + num <= max_sum_allowed:
                    current_sum += num
                else:
                    current_sum = num
                    splits_required += 1

            return splits_required + 1

        left, right = max(nums), sum(nums)
        while left <= right:
            max_sum_allowed = (left + right) // 2

            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_target_split_sum = max_sum_allowed
            else:
                left = max_sum_allowed + 1

        return minimum_target_split_sum


solution = Solution()
assert solution.splitArray([7, 2, 5, 10, 8], 2) == 18
assert solution.splitArray([1, 2, 3, 4, 5], 2) == 9
assert solution.splitArray([1, 4, 4], 3) == 4
