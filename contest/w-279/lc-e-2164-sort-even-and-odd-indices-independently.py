from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)

        odd = nums[1::2]
        odd.sort(reverse=True)
        even = nums[::2]
        even.sort()

        result = []
        for i in range(n // 2):
            result.append(even[i])
            result.append(odd[i])
        if n % 2 != 0:
            result.append(even[n // 2])

        return result


solution = Solution()
assert solution.sortEvenOdd([4,1,2,3,3]) == [2, 3, 3, 1, 4]
assert solution.sortEvenOdd([4,1,2,3]) == [2, 3, 4, 1]
assert solution.sortEvenOdd([2,1]) == [2, 1]
