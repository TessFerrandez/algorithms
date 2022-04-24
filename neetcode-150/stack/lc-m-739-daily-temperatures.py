from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for today, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, day = stack.pop()
                result[day] = today - day
            stack.append((temp, today))

        return result


solution = Solution()
assert solution.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert solution.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert solution.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
