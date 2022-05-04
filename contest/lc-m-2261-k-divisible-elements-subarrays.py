from bisect import bisect_left
from itertools import accumulate
from typing import List


class Solution:
    # doesn't care about duplicates --> not working
    def countDistinct1(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        divisible = [i for i in range(n) if nums[i] % p == 0] + [n]
        print(divisible)

        num_div = len(divisible) - 1
        j = 0
        total = 0
        for i in range(n):
            if i == divisible[j]:
                max_j = min(num_div, j + k)
                j += 1
            else:
                max_j = min(num_div, j + k + 1)
            print(i, divisible[max_j])
            total += divisible[max_j] - i + 1
        return total

    # calculates the wrong number of strings for some cases
    def countDistinct2(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        divisible = [i for i in range(n) if nums[i] % p == 0] + [n]
        num_div = len(divisible) - 1
        sub_arrays = set()

        j = 0
        for i in range(n):
            if i == divisible[j]:
                max_j = min(num_div, j + k)
                j += 1
            else:
                max_j = min(num_div, j + k + 1)
            for m in range(i, divisible[max_j]):
                sub_arrays.add('-'.join(str(d) for d in nums[i: m + 1]))

        return len(sub_arrays)

    # solution with prefix sum - and binary search
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        divisible = [int(num % p == 0) for num in nums]
        prefix_sum = list(accumulate(divisible))

        sub_arrays = set()
        for left, prefix in enumerate(prefix_sum):
            if divisible[left]:
                target = prefix + k
            else:
                target = prefix + 1 + k
            right = bisect_left(prefix_sum, target, lo=left)
            for end in range(left + 1, right + 1):
                sub_array = tuple(nums[left: end])
                if sub_array not in sub_arrays:
                    sub_arrays.add(sub_array)
        return len(sub_arrays)


solution = Solution()
assert solution.countDistinct([2,3,3,2,2], 2, 2) == 11
assert solution.countDistinct([1,2,3,4], 4, 1) == 10
assert solution.countDistinct([16,17,4,12,3], 4, 1) == 14
