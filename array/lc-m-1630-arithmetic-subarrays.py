from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], left: List[int], right: List[int]) -> List[bool]:
        def is_arithmetic(arr):
            arr.sort()
            if len(arr) <= 2:
                return True

            diff = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True

        return [is_arithmetic(nums[left[i]: right[i] + 1]) for i in range(len(left))]


solution = Solution()
assert solution.checkArithmeticSubarrays(nums=[4,6,5,9,3,7], left=[0,0,2], right=[2,3,5]) == [True, False, True]
assert solution.checkArithmeticSubarrays(nums=[-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], left=[0,1,6,4,8,7], right=[4,4,9,7,9,10]) == [False, True, False, False, True, True]
