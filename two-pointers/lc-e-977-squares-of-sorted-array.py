from typing import List


class Solution:
    def sortedSquares_easy(self, nums: List[int]) -> List[int]:
        return sorted([num * num for num in nums])

    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        left, right = 0, len(nums) - 1

        while left <= right:
            if abs(nums[left]) > nums[right]:
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        return result[::-1]


solution = Solution()
assert solution.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert solution.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
