from typing import List


class Solution:
    def maxSatisfied2(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        original_happy = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        best_diff = 0

        # diff if we pick first window
        diff = 0
        for i in range(minutes):
            diff += customers[i] if grumpy[i] == 1 else 0

        best_diff = diff

        for i in range(0, n - minutes):
            diff -= customers[i] if grumpy[i] == 1 else 0
            diff += customers[i + minutes] if grumpy[i + minutes] == 1 else 0
            best_diff = max(best_diff, diff)

        return original_happy + best_diff

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        already_happy = 0

        for i in range(n):
            if not grumpy[i]:
                already_happy += customers[i]
                customers[i] = 0

        max_diff = diff = sum(customers[: minutes])

        # rolling sum
        for i in range(n - minutes):
            diff = diff - customers[i] + customers[i + minutes]
            max_diff = max(diff, max_diff)

        return already_happy + max_diff


solution = Solution()
assert solution.maxSatisfied([4, 10, 10], [1, 1, 0], 2) == 24
assert solution.maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3) == 16
assert solution.maxSatisfied([1], [0], 1) == 1
