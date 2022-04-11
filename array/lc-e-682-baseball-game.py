from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []

        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


solution = Solution()
assert solution.calPoints(["5","2","C","D","+"]) == 30
assert solution.calPoints(["5","-2","4","C","D","9","+","+"]) == 27
assert solution.calPoints(["1"]) == 1
