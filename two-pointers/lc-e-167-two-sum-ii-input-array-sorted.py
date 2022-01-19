from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            to_find = target - numbers[i]
            lower = i + 1
            upper = len(numbers) - 1
            while lower <= upper:
                mid = lower + ((upper - lower) // 2)
                if numbers[mid] == to_find:
                    return [i + 1, mid + 1]
                if numbers[mid] < to_find:
                    lower = mid + 1
                else:
                    upper = mid - 1
        return []


solution = Solution()
assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
assert solution.twoSum([2, 3, 4], 6) == [1, 3]
assert solution.twoSum([-1, 0], -1) == [1, 2]
