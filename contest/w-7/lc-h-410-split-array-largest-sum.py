from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        prefix_sum, cum_sum = 0, []
        n = len(nums)

        if m >= n:
            return max(nums)

        for num in nums:
            prefix_sum += num
            cum_sum.append(prefix_sum)

        cache = {}

        def split(first, m):
            if (first, m) in cache:
                return cache[(first, m)]

            prev = 0 if first == 0 else cum_sum[first - 1]

            if m == 1:
                cache[(first, m)] = cum_sum[-1] - prev
                return cache[(first, m)]

            best = float('inf')
            for i in range(first, n - m + 1):
                curr_sum = cum_sum[i] - prev
                if curr_sum > best:
                    break
                rest_sum = split(i + 1, m - 1)
                best = min(best, max(curr_sum, rest_sum))

            cache[(first, m)] = best
            return cache[(first, m)]

        return split(0, m)


solution = Solution()
assert solution.splitArray([7,2,5,10,8], 2) == 18
assert solution.splitArray([1,2,3,4,5], 2) == 9
assert solution.splitArray([1, 4, 4], 3) == 4
