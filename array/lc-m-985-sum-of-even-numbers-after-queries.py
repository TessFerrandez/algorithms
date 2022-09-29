from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum_even = sum([num for num in nums if num % 2 == 0])
        result = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                sum_even -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                sum_even += nums[idx]

            result.append(sum_even)

        return result


solution = Solution()
assert solution.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]) == [8, 6, 2, 4]
assert solution.sumEvenAfterQueries([1], [[4, 0]]) == [0]
