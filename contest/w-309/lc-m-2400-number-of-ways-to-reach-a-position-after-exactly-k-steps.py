from functools import cache


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        @cache
        def num_ways(start, remaining):
            if remaining == 0 and start == endPos:
                return 1

            if abs(endPos - start) > remaining:
                return 0

            return num_ways(start - 1, remaining - 1) + num_ways(start + 1, remaining - 1)

        diff = abs(endPos - startPos)
        even_diff = diff % 2 == 0
        even_steps = k % 2 == 0

        if even_diff and not even_steps:
            return 0
        if even_steps and not even_diff:
            return 0

        return num_ways(startPos, k) % (10 ** 9 + 7)


solution = Solution()
assert solution.numberOfWays(1, 2, 3) == 3
assert solution.numberOfWays(2, 5, 10) == 0
assert solution.numberOfWays(989, 1000, 99) == 934081896
