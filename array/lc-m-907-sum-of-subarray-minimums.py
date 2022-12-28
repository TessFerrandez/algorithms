from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        stack = []
        sum_of_minimums = 0

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i
                count = (mid - left) * (right - mid)
                sum_of_minimums += (count * arr[mid])
            stack.append(i)
        return sum_of_minimums % MOD


solution = Solution()
assert solution.sumSubarrayMins([11, 81, 94, 43, 3]) == 444
assert solution.sumSubarrayMins([3, 1, 2, 4]) == 17
