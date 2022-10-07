from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        color_stack = [colors[0]]
        time_stack = [neededTime[0]]

        total = 0

        for i in range(1, len(colors)):
            if colors[i] == color_stack[-1]:
                total += min(time_stack[-1], neededTime[i])
                time_stack[-1] = max(time_stack[-1], neededTime[i])
            else:
                color_stack.append(colors[i])
                time_stack.append(neededTime[i])

        return total


solution = Solution()
assert solution.minCost("abaac", [1, 2, 3, 4, 5]) == 3
assert solution.minCost("abc", [1, 2, 3]) == 0
assert solution.minCost("aabaa", [1, 2, 3, 4, 1]) == 2
