from collections import defaultdict
from typing import List


class Solution:
    def printLongestIncreasingSubsequence(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = defaultdict(list)
        longest[0].append([nums[0]])

        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    for lst in longest[j]:
                        longest[i].append(lst + [num])
                elif num <= nums[j] and [num] not in longest[i]:
                    longest[i].append([num])

        res = defaultdict(list)
        for i, lists in longest.items():
            max_len = 0
            for lst in lists:
                max_len = max(max_len, len(lst))
            for lst in lists:
                if len(lst) == max_len:
                    res[i].append(lst)

        print(res)

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(last, i):
            if i == n:
                return 0
            add, not_add = 0, 0
            if nums[i] > last:
                add = 1 + helper(nums[i], i + 1)
            not_add = helper(last, i + 1)

            return max(add, not_add)

        return helper(float('-inf'), 0)


solution = Solution()
solution.printLongestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18])
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
