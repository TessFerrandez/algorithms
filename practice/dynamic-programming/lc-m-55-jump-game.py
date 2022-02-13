from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        can_jump = [False for _ in range(n)]
        can_jump[n - 1] = True

        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if can_jump[i + j]:
                    can_jump[i] = True
                    break

        return can_jump[0]


solution = Solution()
assert solution.canJump([2, 3, 1, 1, 4])
assert not solution.canJump([3, 2, 1, 0, 4])
