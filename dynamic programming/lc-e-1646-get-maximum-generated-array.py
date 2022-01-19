'''
nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.
'''
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0 for _ in range(n + 2)]
        nums[1] = 1

        for i in range(n // 2 + 1):
            nums[2 * i] = nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]

        return max(nums[:n + 1])


solution = Solution()
assert solution.getMaximumGenerated(3) == 2
assert solution.getMaximumGenerated(7) == 3
assert solution.getMaximumGenerated(2) == 1
