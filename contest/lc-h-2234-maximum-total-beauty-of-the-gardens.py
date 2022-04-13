from bisect import bisect_right
from typing import List


class Solution:
    # greedy solution
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers = [min(current, target) for current in flowers]
        flowers.sort()

        n = len(flowers)

        # all beds are full
        if min(flowers) == target:
            return full * n

        # we can fill all flowerbeds
        if newFlowers >= target * n - sum(flowers):
            return max(full * n, full * (n - 1) + partial * (target - 1))

        # build cost array
        cost = [0]
        for i in range(1, n):
            pre = cost[-1]
            cost.append(pre + i * (flowers[i] - flowers[i - 1]))

        # skip all flowerbeds that are full
        right = n - 1
        while flowers[right] == target:
            right -= 1

        # start completing flowerbeds
        result = 0
        while newFlowers >= 0:
            i = min(right, bisect_right(cost, newFlowers) - 1)
            min_incomplete = flowers[i] + (newFlowers - cost[i]) // (i + 1)
            result = max(result, min_incomplete * partial + full * (n - right - 1))

            # complete garden [right], deducting the cost for garden j from newFlowers and moving
            # to the next imcomplete garden
            newFlowers -= (target - flowers[right])
            right -= 1

        return result


solution = Solution()
print(solution.maximumBeauty([1, 3, 1, 1], 7, 6, 12, 1))
print(solution.maximumBeauty([2, 4, 5, 3], 10, 5, 2, 6))
