from typing import List


class Solution:
    # using sort T: O(n log n) M: O(n)
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        nums_copy = nums[::]
        nums_copy.sort()

        start, end = len(nums), 0
        for i in range(len(nums)):
            if nums[i] != nums_copy[i]:
                start = min(i, start)
                end = max(i, end)

        return end - start + 1 if (end - start >= 0) else 0

    # using stack O(n), O(n)
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        stack = []
        start, end = len(nums), 0

        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)

        return end - start + 1 if (end - start > 0) else 0

    # T O(n) M O(1)
    def findUnsortedSubarray3(self, nums: List[int]) -> int:
        min_val, max_val = float('inf'), -float('inf')

        flag = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                flag = True
            if flag:
                min_val = min(min_val, nums[i])

        flag = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                flag = True
            if flag:
                max_val = max(max_val, nums[i])

        for start in range(len(nums)):
            if min_val < nums[start]:
                break

        for end in range(len(nums) - 1, -1, -1):
            if max_val > nums[end]:
                break

        return end - start + 1 if (end - start > 0) else 0

    # T O(n) M O(1) - cleaner
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # largest index not in place
        prev, end = nums[0], 0
        for i in range(n):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]

        # smallest index not in place
        prev, start = nums[-1], n - 1
        for i in range(n - 1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]

        return end - start + 1 if end != 0 else 0


solution = Solution()
assert solution.findUnsortedSubarray([1, 2, 3, 3, 3]) == 0
assert solution.findUnsortedSubarray([1, 3, 2, 3, 3, 3]) == 2
assert solution.findUnsortedSubarray([1, 3, 3, 3, 2, 2, 2]) == 6
assert solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
assert solution.findUnsortedSubarray([6, 2, 4, 8, 10, 9, 15]) == 6
assert solution.findUnsortedSubarray([6, 2, 4, 8, 10, 15, 9]) == 7
assert solution.findUnsortedSubarray([1, 2, 3, 4]) == 0
assert solution.findUnsortedSubarray([1]) == 0
