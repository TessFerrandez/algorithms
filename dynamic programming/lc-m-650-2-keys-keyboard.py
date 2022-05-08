from functools import cache


class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def get_min_steps(current, target, clip_board):
            if current == target:
                return 0
            if current > target:
                return float('inf')
            copy = float('inf') if current == clip_board else get_min_steps(current, target, current)
            paste = float('inf') if clip_board == 0 else get_min_steps(current + clip_board, target, clip_board)
            return min(copy, paste) + 1

        return get_min_steps(1, n, 0)


solution = Solution()
assert solution.minSteps(3) == 3
assert solution.minSteps(1) == 0
