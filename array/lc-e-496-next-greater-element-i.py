'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
'''
from typing import List


class Solution:
    # O (n * n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indices = {num: i for i, num in enumerate(nums2)}

        n = len(nums2)
        result = []

        for num in nums1:
            result.append(-1)
            for i in range(indices[num] + 1, n):
                if nums2[i] > num:
                    result[-1] = nums2[i]
                    break

        return result

    # O (n + m)
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        ex. 9, 8, 7, 3, 2, 1, 6
        1. keep feeding "needs_greater" while the numbers are decreasing
            9, 8, 7, 3, 2, 1
        2. when we have a "greater" number (6) - pop all the nums below it (1, 2, 3)
           these numbers will have 6 as their next greater number
        3. every number we haven't found a greater number for => greater = -1
        '''
        indices = {num: i for i, num in enumerate(nums1)}

        next_greater = [-1] * len(nums1)
        needs_greater = []
        for num in nums2:
            while needs_greater and needs_greater[-1] < num:
                prev_num = needs_greater.pop()
                next_greater[indices[prev_num]] = num

            if num in indices:
                needs_greater.append(num)

        while needs_greater:
            prev_num = needs_greater.pop()
            next_greater[indices[prev_num]] = -1

        return next_greater


solution = Solution()
assert solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
assert solution.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
