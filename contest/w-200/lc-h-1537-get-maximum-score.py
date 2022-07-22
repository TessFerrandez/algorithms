from typing import List


class Solution:
    def maxSum2(self, nums1: List[int], nums2: List[int]) -> int:
        vals = {}

        for i, num in enumerate(nums1):
            vals[num] = [i]

        duplicates = []
        for i, num in enumerate(nums2):
            if num in vals:
                duplicates.append(num)
                vals[num].append(i)

        prev1, prev2 = 0, 0
        max_score = 0
        for duplicate in duplicates:
            i1, i2 = vals[duplicate]

            sum1 = 0 if i1 == prev1 else sum(nums1[prev1: i1])
            prev1 = i1

            sum2 = 0 if i2 == prev2 else sum(nums2[prev2: i2])
            prev2 = i2

            max_score += max(sum1, sum2)

        max_score += max(sum(nums1[prev1:]), sum(nums2[prev2:]))
        return max_score % (10 ** 9 + 7)

    # with prefix sum
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_map = {}

        prefix_sum = 0
        for num in nums1:
            prefix_sum += num
            nums1_map[num] = prefix_sum

        max_score = 0
        prev1, prev2 = 0, 0

        prefix_sum2 = 0
        for num in nums2:
            prefix_sum2 += num
            if num in nums1_map:
                max_score += max(nums1_map[num] - prev1, prefix_sum2 - prev2)
                prev1 = nums1_map[num]
                prev2 = prefix_sum2

        max_score += max(nums1_map[nums1[-1]] - prev1, prefix_sum2 - prev2)
        return max_score % (10 ** 9 + 7)


solution = Solution()
assert solution.maxSum([2, 4, 5, 8, 10], [4, 6, 8, 9]) == 30
assert solution.maxSum([1, 3, 5, 7, 9], [3, 5, 100]) == 109
assert solution.maxSum([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == 40
