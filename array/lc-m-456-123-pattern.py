'''
we want to find a subseq (s1, s2, s3) such that s1 < s3 < s2
so we need to find an s2 - followed by one larger and one smaller
'''
from typing import List


class Solution:
    # one pass with stack s1 < s3 < s2
    def find132pattern1(self, nums: List[int]) -> bool:
        s3 = -float('inf')

        # stack has potential s2s
        s2s = []

        for s1_idx in range(len(nums) - 1, -1, -1):
            if nums[s1_idx] < s3:
                return True
            else:
                while s2s and nums[s1_idx] > s2s[-1]:
                    s3 = s2s.pop()
                s2s.append(nums[s1_idx])

        return False

    # brute force O(n^3)
    def find132pattern2(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] < nums[k] < nums[j]:
                        return True

    # O(n^2)
    def find132pattern3(self, nums: List[int]) -> bool:
        min_val = float('inf')

        for j in range(len(nums)):
            min_val = min(min_val, nums[j])
            if min_val == nums[j]:
                continue
            for k in range(len(nums) - 1, j, -1):
                if min_val < nums[k] < nums[j]:
                    return True
        return False

    # O(n) with prefix sum
    def find132pattern4(self, nums: List[int]) -> bool:
        mins = nums[::]

        for i in range(1, len(nums)):
            mins[i] = min(mins[i - 1], nums[i - 1])

        top = len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] <= mins[j]:
                continue
            while top < len(nums) and mins[top] <= mins[j]:
                top += 1
            if top < len(nums) and nums[j] > mins[top]:
                return True
            top -= 1
            mins[top] = nums[j]

        return False

    # O(n) with without the explicit prefix array
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        top = n
        third = -float('inf')

        for i in range(n - 1, -1, -1):
            if nums[i] < third:
                return True
            while top < n and nums[i] > nums[top]:
                third = nums[top]
                top += 1
            top -= 1
            nums[top] = nums[i]
        return False


solution = Solution()
assert not solution.find132pattern([1, 2, 3, 4])
assert solution.find132pattern([3, 1, 4, 2])
assert solution.find132pattern([-1, 3, 2, 0])
