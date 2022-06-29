from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)


solution = Solution()
assert solution.checkPossibility([4, 2, 3])
assert not solution.checkPossibility([4, 2, 1])
