from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        def searchInsert(nums: List[int], target: int) -> int:
            low, high = 0, len(nums)

            while low < high:
                mid = (low + high) // 2

                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid

            return low

        arr2.sort()
        n = len(arr2)

        count = 0

        for num in arr1:
            i = searchInsert(arr2, num)
            if i == 0 and num + d < arr2[0]:
                count += 1
            elif i == n and arr2[-1] + d < num:
                count += 1
            elif arr2[i - 1] + d < num and num + d < arr2[i]:
                count += 1

        return count


solution = Solution()
assert solution.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2) == 2
assert solution.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3) == 2
assert solution.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6) == 1
