from typing import List


class Solution:
    # my contest solution
    def minimumAverageDifference1(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sums = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefix_sums.append(prefix_sum)

        postfix_sums = []
        postfix_sum = 0
        for i in range(n - 1, -1, -1):
            postfix_sum += nums[i]
            postfix_sums.append(postfix_sum)
        postfix_sums = postfix_sums[::-1]

        min_avg = float('inf')
        best = -1
        for i in range(n - 1):
            curr_avg = abs(prefix_sums[i] // (i + 1) - postfix_sums[i + 1] // (n - i - 1))
            if curr_avg < min_avg:
                min_avg = curr_avg
                best = i

        last_avg = prefix_sums[-1] // n
        if last_avg < min_avg:
            best = n - 1

        return best

    # more concise and O(1) space
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n, min_avg_diff, index = len(nums), float('inf'), -1
        sum_from_end = sum(nums)
        sum_from_front = 0

        for i, num in enumerate(nums):
            sum_from_front += num
            sum_from_end -= num
            avg_first = sum_from_front // (i + 1)
            avg_last = 0 if i == (n - 1) else sum_from_end // (n - i - 1)

            if abs(avg_first - avg_last) < min_avg_diff:
                min_avg_diff = abs(avg_first - avg_last)
                index = i

        return index


solution = Solution()
assert solution.minimumAverageDifference([2,5,3,9,5,3]) == 3
assert solution.minimumAverageDifference([0]) == 0
