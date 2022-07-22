from itertools import accumulate
from typing import List


class Solution:
    # my solution (TLE)
    def countSubarrays1(self, nums: List[int], k: int) -> int:
        prefix = list(accumulate(nums))

        count = 0
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                the_sum = prefix[end] if start == 0 else prefix[end] - prefix[start - 1]
                the_len = end - start + 1
                if the_len * the_sum < k:
                    count += 1
                else:
                    break
        return count

    # sliding window
    # T O(n) S O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = current = i = 0

        for j in range(len(nums)):
            current += nums[j]
            while current * (j - i + 1) >= k:
                current -= nums[i]
                i += 1
            result += j - i + 1
        return result


solution = Solution()
print(solution.countSubarrays([2, 1, 4, 3, 5], 10))
print(solution.countSubarrays([1, 1, 1], 5))
