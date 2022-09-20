class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        def calculate_steps(min_val, max_val):
            steps = 0

            while min_val <= n:
                steps += min(n + 1, max_val) - min_val
                min_val *= 10
                max_val *= 10

            return steps

        while k > 0:
            steps = calculate_steps(current, current + 1)

            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1

        return current


solution = Solution()
assert solution.findKthNumber(13, 2) == 10
assert solution.findKthNumber(1, 1) == 1
