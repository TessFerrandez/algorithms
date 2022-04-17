from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def find(start, end, target):
            low, high = start, end
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target:
                    return mid
                if numbers[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1

        n = len(numbers)

        for i in range(n - 1):
            i2 = find(i + 1, n - 1, target - numbers[i])
            if i2 != -1:
                return [i + 1, i2 + 1]
        return [-1, -1]


solution = Solution()
assert solution.twoSum([5, 25, 75], 100) == [2, 3]
assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
assert solution.twoSum([2, 3, 4], 6) == [1, 3]
assert solution.twoSum([-1, 0], -1) == [1, 2]
