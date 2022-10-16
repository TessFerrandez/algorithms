from typing import List


class Solution:
    def smallerSum(self, n: int, arr: List[int]) -> List[int]:
        sorted_nums = sorted(arr)
        sums = {}

        current_sum = 0
        for num in sorted_nums:
            if num not in sums:
                sums[num] = current_sum
            current_sum += num

        result = []
        for num in arr:
            result.append(sums[num])

        return result


solution = Solution()
assert solution.smallerSum(3, [1, 2, 3]) == [0, 1, 3]
assert solution.smallerSum(2, [4, 4]) == [0, 0]
