from math import comb
from typing import List


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        '''
        separate all elements into two lists (lower or higher than root)
        recurse on left and right sub-lists
        the combination is for the macro ordering between left and right, and recursive factors are for the internal ordering of left and right
        - finally -1 to avoid counting the original order
        '''
        MOD = 10 ** 9 + 7

        def ways_to_interleave(nums1, nums2):
            '''
            total ways to interleave two arrays maintaining order
            '''
            m, n = len(nums1), len(nums2)
            total_items = m + n
            items_to_choose = m
            return comb(total_items, items_to_choose)

        def count_ways(subsequence):
            if not subsequence:
                return 1
            root = subsequence[0]
            left = [number for number in subsequence if number < root]
            right = [number for number in subsequence if number > root]
            ways_to_arrange_left = count_ways(left)
            ways_to_arrange_right = count_ways(right)
            return ways_to_arrange_left * ways_to_arrange_right * ways_to_interleave(left, right)

        return (count_ways(nums) - 1) % MOD


solution = Solution()
assert solution.numOfWays([2,1,3]) == 1
assert solution.numOfWays([3,4,5,1,2]) == 5
assert solution.numOfWays([1,2,3]) == 0
